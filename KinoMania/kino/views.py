from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q
from datetime import date, datetime, timedelta

from .models import Film, Seans, Rezerwacja, Gatunek
from .forms import RegisterForm


class FilmyListView(ListView):
    """List all movies"""
    model = Film
    template_name = 'kino/filmy_list.html'
    context_object_name = 'filmy'
    paginate_by = 12

    def get_queryset(self):
        queryset = Film.objects.all().prefetch_related('gatunek', 'aktorzy')
        
        # Search by title or description
        search = self.request.GET.get('search')
        if search:
            queryset = queryset.filter(
                Q(tytul__icontains=search) | Q(opis__icontains=search)
            )
        
        # Filter by genre
        gatunek_id = self.request.GET.get('gatunek')
        if gatunek_id:
            queryset = queryset.filter(gatunek__id=gatunek_id)
        
        return queryset.order_by('-data_premiery').distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gatunki'] = Gatunek.objects.all()
        context['search'] = self.request.GET.get('search', '')
        context['selected_gatunek'] = self.request.GET.get('gatunek', '')
        return context


class FilmDetailView(DetailView):
    """Movie detail page"""
    model = Film
    template_name = 'kino/film_detail.html'
    context_object_name = 'film'
    slug_field = 'id'
    slug_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        film = self.get_object()
        
        # Get upcoming screenings
        now = datetime.now()
        context['seanse'] = film.seanse.filter(
            czas_rozpoczecia__gte=now
        ).order_by('czas_rozpoczecia')
        
        return context


class SeansyListView(ListView):
    """List screenings for a given day or upcoming"""
    model = Seans
    template_name = 'kino/seanse_list.html'
    context_object_name = 'seanse'
    paginate_by = 20

    def get_queryset(self):
        queryset = Seans.objects.select_related('film').filter(
            czas_rozpoczecia__gte=datetime.now()
        ).order_by('czas_rozpoczecia')
        
        # Filter by date if provided
        data = self.request.GET.get('data')
        if data:
            try:
                filter_date = datetime.strptime(data, '%Y-%m-%d').date()
                queryset = queryset.filter(czas_rozpoczecia__date=filter_date)
            except ValueError:
                pass
        
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = date.today()
        context['next_days'] = [date.today() + timedelta(days=i) for i in range(7)]
        context['selected_date'] = self.request.GET.get('data', '')
        return context


@login_required
def rezerwuj_bilet(request, seans_id):
    """Make a reservation"""
    seans = get_object_or_404(Seans, id=seans_id)
    
    if request.method == 'POST':
        try:
            ilosc_miejsc = int(request.POST.get('ilosc_miejsc', 1))
            
            if ilosc_miejsc < 1:
                messages.error(request, 'Ilość miejsc musi być większa od 0.')
                return redirect('seans_detail', pk=seans_id)
            
            if ilosc_miejsc > seans.dostepne_miejsca:
                messages.error(
                    request, 
                    f'Niedostępna ilość miejsc. Dostępne: {seans.dostepne_miejsca}'
                )
                return redirect('seans_detail', pk=seans_id)
            
            # Check for existing reservation
            existing = Rezerwacja.objects.filter(
                seans=seans,
                uzytkownik=request.user,
                status__in=['pending', 'confirmed']
            ).first()
            
            if existing:
                messages.warning(request, 'Masz już rezerwację na ten seans!')
                return redirect('seans_detail', pk=seans_id)
            
            # Create reservation
            rezerwacja = Rezerwacja.objects.create(
                seans=seans,
                uzytkownik=request.user,
                ilosc_miejsc=ilosc_miejsc,
                status='pending'
            )
            
            # Update available seats
            seans.zmien_dostepne_miejsca(ilosc_miejsc)
            
            messages.success(
                request, 
                f'Rezerwacja na {ilosc_miejsc} miejsc(a) została utworzona!'
            )
            return redirect('rezerwacje_lista')
            
        except (ValueError, TypeError):
            messages.error(request, 'Błąd przy rezerwacji.')
            return redirect('seans_detail', pk=seans_id)
    
    return redirect('seans_detail', pk=seans_id)


class RezerwacjaDetailView(DetailView):
    """Screening detail with reservation"""
    model = Seans
    template_name = 'kino/seans_detail.html'
    context_object_name = 'seans'
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        seans = self.get_object()
        context['user_reservation'] = None
        
        if self.request.user.is_authenticated:
            context['user_reservation'] = Rezerwacja.objects.filter(
                seans=seans,
                uzytkownik=self.request.user,
                status__in=['pending', 'confirmed']
            ).first()
        
        return context


@login_required
def moje_rezerwacje(request):
    """User's reservations"""
    rezerwacje = Rezerwacja.objects.filter(
        uzytkownik=request.user
    ).select_related('seans__film').order_by('-data_rezerwacji')
    
    # Filter by status if provided
    status_filter = request.GET.get('status')
    if status_filter:
        rezerwacje = rezerwacje.filter(status=status_filter)
    
    context = {
        'rezerwacje': rezerwacje,
        'statuses': Rezerwacja.STATUS_CHOICES,
        'selected_status': status_filter,
    }
    
    return render(request, 'kino/my_reservations.html', context)


@login_required
def anuluj_rezerwacje(request, rezerwacja_id):
    """Cancel a reservation"""
    rezerwacja = get_object_or_404(Rezerwacja, id=rezerwacja_id)
    
    if rezerwacja.uzytkownik != request.user:
        messages.error(request, 'Nie masz uprawnień do tej operacji.')
        return redirect('rezerwacje_lista')
    
    if rezerwacja.status == 'cancelled':
        messages.warning(request, 'Rezerwacja została już anulowana.')
        return redirect('rezerwacje_lista')
    
    if request.method == 'POST':
        rezerwacja.cancel()
        messages.success(request, 'Rezerwacja została anulowana.')
        return redirect('rezerwacje_lista')
    
    context = {'rezerwacja': rezerwacja}
    return render(request, 'kino/cancel_reservation.html', context)


def home(request):
    """Home page - recently added films"""
    filmy_najnowsze = Film.objects.all().order_by('-data_dodania')[:6]
    seanse_jutro = Seans.objects.filter(
        czas_rozpoczecia__date=date.today() + timedelta(days=1)
    ).select_related('film')[:5]
    
    context = {
        'filmy_najnowsze': filmy_najnowsze,
        'seanse_jutro': seanse_jutro,
    }
    
    return render(request, 'kino/home.html', context)


def register(request):
    """User registration"""
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Konto zostało utworzone. Możesz się teraz zalogować.')
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, 'kino/register.html', {'form': form})


@login_required
def potwierdz_rezerwacje(request, rezerwacja_id):
    """Admin action to confirm reservation (simplified for demo)"""
    rezerwacja = get_object_or_404(Rezerwacja, id=rezerwacja_id)
    
    if not request.user.is_staff:
        messages.error(request, 'Nie masz uprawnień do tej operacji.')
        return redirect('home')
    
    if request.method == 'POST':
        rezerwacja.confirm()
        messages.success(request, 'Rezerwacja została potwierdzona.')
        return redirect('rezerwacje_lista')
    
    context = {'rezerwacja': rezerwacja}
    return render(request, 'kino/confirm_reservation.html', context)


