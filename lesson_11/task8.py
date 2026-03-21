# Zadanie 8 – Hierarchia instrumentów muzycznych
# Zaprojektuj hierarchię klas: Instrument -> Strunowy i Dety. Następnie Gitara (dziedziczy po
# Strunowy) i Trabka (dziedziczy po Dety). Klasa Instrument powinna mieć metodę graj(),
# która zwraca ogólny komunikat. Każda kolejna klasa w hierarchii powinna nadpisywać tę metodę, dodając coś od siebie i wywołując wersję z klasy nadrzędnej za pomocą super().graj().
# Instrument.graj() -> "Wydaje dźwięk."
# Strunowy.graj() -> "Wydaje dźwięk. [Szarpnięcie struny]"
# Gitara.graj() -> "Wydaje dźwięk. [Szarpnięcie struny] [Akord G-dur]" (challenge)

class Instrument:
    def graj(self):
        return f"Wydaje dźwięk."

class Strunowy(Instrument):
    def graj(self):
        s_tekst = super().graj()
        return f"{s_tekst} [Szarpnięcie struny]"

class Dety(Instrument):
    def graj(self):
        d_tekst = super().graj()
        return f"{d_tekst} [Zadęcie]"

class Gitara(Strunowy):
    def graj(self):
        g_tekst = super().graj()
        return f"{g_tekst} [Akord G-dur]"

class Trabka(Dety):
    def graj(self):
        t_tekst = super().graj()
        return f"{t_tekst} [Krótka fanfara]"
    
gitara = Gitara()
print(gitara.graj())