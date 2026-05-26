# Zadanie 1 – Analiza Middleware
#
# SessionMiddleware – odpowiada za obsługę sesji użytkownika: wczytuje dane
# sesji z ciasteczka przy każdym żądaniu i zapisuje je z powrotem po jego
# obsłużeniu, dzięki czemu Django "pamięta" zalogowanego użytkownika między
# kolejnymi zapytaniami HTTP.
#
# AuthenticationMiddleware – odpowiada za przypisanie zalogowanego użytkownika
# do obiektu request: dla każdego przychodzącego żądania odczytuje identyfikator
# użytkownika z sesji i ustawia atrybut request.user, który jest następnie
# dostępny w widokach i szablonach.
