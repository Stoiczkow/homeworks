from dataclasses import dataclass



@dataclass
class Film:
    tytul: str
    rezyser: str # (string)
    rok_produkcji: int

syfy = Film("Terminator", "Cameron", "1984")

komedia = Film ("Chłopaki nie płaczą", "Lubaszenko", 1997 )

print(syfy)

print(komedia)

