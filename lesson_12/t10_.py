# Zadanie 10 – Metaklasa walidująca
# Stwórz metaklasę MetaWalidujMetody, która podczas tworzenia nowej klasy sprawdza, czy
# wszystkie jej metody (poza metodami "magicznymi", czyli zaczynającymi się od __) mają
# docstring. Jeśli któraś metoda go nie ma, metaklasa powinna podnieść TypeError z
# informacją, która metoda wymaga dokumentacji. Przetestuj ją, tworząc klasę z poprawnie i
# niepoprawnie udokumentowanymi metodami.