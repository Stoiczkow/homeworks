# Zadanie 15 – Prosty web crawler
# Napisz prosty crawler, który zaczyna od jednego adresu URL. Pobiera jego zawartość,
# znajduje w niej wszystkie linki do tej samej domeny, a następnie dodaje je do kolejki do
# odwiedzenia. Użyj puli wątków do jednoczesnego pobierania stron z kolejki. Ogranicz liczbę
# odwiedzonych stron do np. 50, aby nie "zalać" serwera. Użyj bezpiecznej wątkowo kolejki i
# zbioru (set) do przechowywania już odwiedzonych linków.