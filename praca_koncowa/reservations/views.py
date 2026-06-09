from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from datetime import date
# from django.http import Http404
from .models import Screening, Reservation

# 1. Rejestracja użytkownika
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Konto użytkownika {username} zostało utworzone!")
            return redirect('login') 
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


# 2. Harmonogram seansów na dany dzień
def harmonogram_dnia(request):

    wybrany_dzien = request.GET.get('data')
    if wybrany_dzien:
        try:
            result = date.fromisoformat(wybrany_dzien)
        except ValueError:
            result = date.today()
    else:
        result = date.today()

    seanse = Screening.objects.filter(date_screening=result).select_related('movie')

    return render(request, 'reservations/harmonogram.html', {
        'seanse': seanse,
        'wybrany_dzien': result
    })


# 3. System rezerwacji biletów (Tylko dla zalogowanych) 

@login_required
def zarezerwuj_bilet(request, seans_id):
    seans = Screening.objects.get(id=seans_id)

    if request.method == 'POST':
        ilosc = int(request.POST.get('ilosc_miejsc', 0))

        if ilosc == 0:
            return redirect('show_all_movies')

        if ilosc < 0:
            messages.error(request, "Musisz wybrac przynajmniej jeden bilet.")
            return redirect('zarezerwuj_bilet', seans_id=seans.id)

        Reservation.objects.create(
            user=request.user,
            screening=seans,
            number_of_places=ilosc
        )
        messages.success(request, "Bilety zostały pomyślnie zarezerwowane!")
        return redirect('panel_uzytkownika')

    return render(request, 'reservations/rezerwacja.html', {'seans': seans})


@login_required
def panel_uzytkownika(request):
    # Pobieramy rezerwacje przypisane wyłącznie do zalogowanego użytkownika
    moje_rezerwacje = request.user.reservations.all().select_related('screening__movie')
    
    return render(request, 'reservations/panel.html', {
        'rezerwacje': moje_rezerwacje
    })