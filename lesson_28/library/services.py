from datetime import timedelta

from django.db import transaction
from django.utils import timezone

from .models import Copy, Reservation


class ReservationError(Exception):
    pass


def release_expired_reservations():
    today = timezone.localdate()
    expired_reservations = Reservation.objects.select_related('copy').filter(
        status=Reservation.Status.ACTIVE,
        valid_until__lt=today,
    )

    for reservation in expired_reservations:
        reservation.status = Reservation.Status.FINISHED
        reservation.save(update_fields=['status'])
        if reservation.copy.status == Copy.Status.RESERVED:
            reservation.copy.status = Copy.Status.AVAILABLE
            reservation.copy.save(update_fields=['status'])


def reserve_copy_for_user(copy_id, user):
    release_expired_reservations()

    with transaction.atomic():
        copy = Copy.objects.select_for_update().select_related('book').get(pk=copy_id)
        if copy.status != Copy.Status.AVAILABLE:
            raise ReservationError('Ten egzemplarz nie jest już dostępny.')

        reservation = Reservation.objects.create(
            user=user,
            copy=copy,
            valid_until=timezone.localdate() + timedelta(days=14),
        )
        copy.status = Copy.Status.RESERVED
        copy.save(update_fields=['status'])
        return reservation


def cancel_reservation(reservation, user):
    if reservation.user != user:
        raise ReservationError('Nie możesz anulować cudzej rezerwacji.')
    if reservation.status != Reservation.Status.ACTIVE:
        raise ReservationError('Tę rezerwację już wcześniej zamknięto.')

    with transaction.atomic():
        reservation.status = Reservation.Status.CANCELLED
        reservation.save(update_fields=['status'])
        copy = reservation.copy
        copy.status = Copy.Status.AVAILABLE
        copy.save(update_fields=['status'])