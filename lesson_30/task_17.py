# Zadanie 17 – Komunikacja dwukierunkowa (Pipe)
# Użyj multiprocessing.Pipe do stworzenia dwukierunkowej komunikacji. Proces nadrzędny
# wysyła do procesu potomnego listę liczb. Proces potomny oblicza ich sumę i średnią, a
# następnie odsyła krotkę z wynikami ((suma, srednia)) do procesu nadrzędnego, który je
# drukuje