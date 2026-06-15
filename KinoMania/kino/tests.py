from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, timedelta
from kino.models import Film, Gatunek, Aktor, Rezyser, Seans, Rezerwacja


class GatunekModelTest(TestCase):
    """Test Gatunek (Genre) model"""
    
    def setUp(self):
        self.gatunek = Gatunek.objects.create(nazwa='Akcja')
    
    def test_gatunek_creation(self):
        """Test if genre is created correctly"""
        self.assertEqual(self.gatunek.nazwa, 'Akcja')
        self.assertEqual(str(self.gatunek), 'Akcja')
    
    def test_unique_gatunek_nazwa(self):
        """Test if genre name is unique"""
        with self.assertRaises(Exception):
            Gatunek.objects.create(nazwa='Akcja')


class AktorModelTest(TestCase):
    """Test Aktor (Actor) model"""
    
    def setUp(self):
        self.aktor = Aktor.objects.create(imie_nazwisko='Tom Hanks')
    
    def test_aktor_creation(self):
        """Test if actor is created correctly"""
        self.assertEqual(self.aktor.imie_nazwisko, 'Tom Hanks')
        self.assertEqual(str(self.aktor), 'Tom Hanks')


class RezyserModelTest(TestCase):
    """Test Rezyser (Director) model"""
    
    def setUp(self):
        self.rezyser = Rezyser.objects.create(imie_nazwisko='Steven Spielberg')
    
    def test_rezyser_creation(self):
        """Test if director is created correctly"""
        self.assertEqual(self.rezyser.imie_nazwisko, 'Steven Spielberg')
        self.assertEqual(str(self.rezyser), 'Steven Spielberg')


class FilmModelTest(TestCase):
    """Test Film (Movie) model"""
    
    def setUp(self):
        self.gatunek = Gatunek.objects.create(nazwa='Akcja')
        self.rezyser = Rezyser.objects.create(imie_nazwisko='Spielberg')
        self.aktor = Aktor.objects.create(imie_nazwisko='Tom Hanks')
        
        self.film = Film.objects.create(
            tytul='Inception',
            opis='A great movie',
            data_premiery=datetime.now().date(),
            rezyser=self.rezyser
        )
        self.film.gatunek.add(self.gatunek)
        self.film.aktorzy.add(self.aktor)
    
    def test_film_creation(self):
        """Test if movie is created correctly"""
        self.assertEqual(self.film.tytul, 'Inception')
        self.assertEqual(self.film.rezyser, self.rezyser)
    
    def test_film_gatunek_relation(self):
        """Test many-to-many relationship with genre"""
        self.assertIn(self.gatunek, self.film.gatunek.all())
    
    def test_film_aktorzy_relation(self):
        """Test many-to-many relationship with actors"""
        self.assertIn(self.aktor, self.film.aktorzy.all())


class SeansModelTest(TestCase):
    """Test Seans (Screening) model"""
    
    def setUp(self):
        self.rezyser = Rezyser.objects.create(imie_nazwisko='Spielberg')
        self.film = Film.objects.create(
            tytul='Inception',
            opis='A great movie',
            data_premiery=datetime.now().date(),
            rezyser=self.rezyser
        )
        
        self.seans = Seans.objects.create(
            film=self.film,
            czas_rozpoczecia=datetime.now() + timedelta(days=1),
            cena=25.00,
            liczba_miejsc=50,
            dostepne_miejsca=50
        )
    
    def test_seans_creation(self):
        """Test if screening is created correctly"""
        self.assertEqual(str(self.seans), f"{self.film.tytul} - {self.seans.czas_rozpoczecia}")
        self.assertEqual(self.seans.dostepne_miejsca, 50)
    
    def test_zmien_dostepne_miejsca(self):
        """Test updating available seats"""
        self.seans.zmien_dostepne_miejsca(5)
        self.assertEqual(self.seans.dostepne_miejsca, 45)


class RezerwacjaModelTest(TestCase):
    """Test Rezerwacja (Reservation) model"""
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        
        self.rezyser = Rezyser.objects.create(imie_nazwisko='Spielberg')
        self.film = Film.objects.create(
            tytul='Inception',
            opis='A great movie',
            data_premiery=datetime.now().date(),
            rezyser=self.rezyser
        )
        
        self.seans = Seans.objects.create(
            film=self.film,
            czas_rozpoczecia=datetime.now() + timedelta(days=1),
            cena=25.00,
            liczba_miejsc=50,
            dostepne_miejsca=50
        )
        
        self.rezerwacja = Rezerwacja.objects.create(
            seans=self.seans,
            uzytkownik=self.user,
            ilosc_miejsc=2,
            status='pending'
        )
    
    def test_rezerwacja_creation(self):
        """Test if reservation is created correctly"""
        self.assertEqual(self.rezerwacja.uzytkownik, self.user)
        self.assertEqual(self.rezerwacja.ilosc_miejsc, 2)
        self.assertEqual(self.rezerwacja.status, 'pending')
    
    def test_rezerwacja_confirm(self):
        """Test confirming reservation"""
        self.rezerwacja.confirm()
        self.assertEqual(self.rezerwacja.status, 'confirmed')
    
    def test_rezerwacja_cancel(self):
        """Test cancelling reservation"""
        initial_seats = self.seans.dostepne_miejsca
        self.rezerwacja.cancel()
        self.assertEqual(self.rezerwacja.status, 'cancelled')
        
        # Refresh from database
        self.seans.refresh_from_db()
        self.assertEqual(self.seans.dostepne_miejsca, initial_seats + 2)


class FilmyListViewTest(TestCase):
    """Test movies list view"""
    
    def setUp(self):
        self.client = Client()
        self.gatunek = Gatunek.objects.create(nazwa='Akcja')
        self.rezyser = Rezyser.objects.create(imie_nazwisko='Spielberg')
        
        self.film = Film.objects.create(
            tytul='Inception',
            opis='A great movie',
            data_premiery=datetime.now().date(),
            rezyser=self.rezyser
        )
        self.film.gatunek.add(self.gatunek)
    
    def test_filmy_list_view(self):
        """Test movies list view renders correctly"""
        response = self.client.get(reverse('filmy_lista'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'kino/filmy_list.html')
        self.assertIn(self.film, response.context['filmy'])
    
    def test_search_functionality(self):
        """Test search functionality"""
        response = self.client.get(reverse('filmy_lista'), {'search': 'Inception'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.film, response.context['filmy'])


class FilmDetailViewTest(TestCase):
    """Test movie detail view"""
    
    def setUp(self):
        self.client = Client()
        self.rezyser = Rezyser.objects.create(imie_nazwisko='Spielberg')
        self.film = Film.objects.create(
            tytul='Inception',
            opis='A great movie',
            data_premiery=datetime.now().date(),
            rezyser=self.rezyser
        )
    
    def test_film_detail_view(self):
        """Test movie detail view"""
        response = self.client.get(reverse('film_detail', args=[self.film.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'kino/film_detail.html')
        self.assertEqual(response.context['film'], self.film)


class RezerwujBiletViewTest(TestCase):
    """Test reservation creation view"""
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        
        self.rezyser = Rezyser.objects.create(imie_nazwisko='Spielberg')
        self.film = Film.objects.create(
            tytul='Inception',
            opis='A great movie',
            data_premiery=datetime.now().date(),
            rezyser=self.rezyser
        )
        
        self.seans = Seans.objects.create(
            film=self.film,
            czas_rozpoczecia=datetime.now() + timedelta(days=1),
            cena=25.00,
            liczba_miejsc=50,
            dostepne_miejsca=50
        )
    
    def test_reservation_requires_login(self):
        """Test that reservation requires login"""
        response = self.client.post(
            reverse('rezerwuj_bilet', args=[self.seans.id]),
            {'ilosc_miejsc': 2}
        )
        self.assertEqual(response.status_code, 302)  # Redirect to login
    
    def test_create_reservation(self):
        """Test creating a reservation"""
        self.client.login(username='testuser', password='testpass123')
        
        response = self.client.post(
            reverse('rezerwuj_bilet', args=[self.seans.id]),
            {'ilosc_miejsc': 2}
        )
        
        self.assertEqual(response.status_code, 302)  # Redirect after success
        
        rezerwacja = Rezerwacja.objects.filter(
            uzytkownik=self.user,
            seans=self.seans
        ).first()
        
        self.assertIsNotNone(rezerwacja)
        self.assertEqual(rezerwacja.ilosc_miejsc, 2)


class MojeRezerwacjeViewTest(TestCase):
    """Test user reservations view"""
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        
        self.rezyser = Rezyser.objects.create(imie_nazwisko='Spielberg')
        self.film = Film.objects.create(
            tytul='Inception',
            opis='A great movie',
            data_premiery=datetime.now().date(),
            rezyser=self.rezyser
        )
        
        self.seans = Seans.objects.create(
            film=self.film,
            czas_rozpoczecia=datetime.now() + timedelta(days=1),
            cena=25.00,
            liczba_miejsc=50,
            dostepne_miejsca=50
        )
        
        self.rezerwacja = Rezerwacja.objects.create(
            seans=self.seans,
            uzytkownik=self.user,
            ilosc_miejsc=2,
            status='confirmed'
        )
    
    def test_reservations_list_requires_login(self):
        """Test that reservations list requires login"""
        response = self.client.get(reverse('rezerwacje_lista'))
        self.assertEqual(response.status_code, 302)  # Redirect to login
    
    def test_reservations_list_view(self):
        """Test user reservations list"""
        self.client.login(username='testuser', password='testpass123')
        
        response = self.client.get(reverse('rezerwacje_lista'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'kino/my_reservations.html')
        self.assertIn(self.rezerwacja, response.context['rezerwacje'])

