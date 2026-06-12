"""
Tworzenie struktury folderów:
Użyj pathlib, aby stworzyć strukturę:
Projekt/src , Projekt/data , Projekt/docs
"""

from pathlib import Path

base = Path("Projekt")

for folder in ["src", "data", "docs"]:
    (base / folder).mkdir(parents=True, exist_ok=True)
