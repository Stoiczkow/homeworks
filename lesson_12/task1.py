from dataclasses import dataclass


@dataclass
class Film:
    tytul: str
    rezyser: str 
    rok_produkcji: int

scifi = Film("Terminator", "Cameron", "1984")

komedia = Film ("Chłopaki nie płaczą", "Lubaszenko", 1997 )

print(scifi)

print(komedia)