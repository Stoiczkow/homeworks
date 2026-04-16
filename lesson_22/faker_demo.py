# Zadanie 5 – samodzielny skrypt testujacy biblioteke Faker
# Uruchom: python faker_demo.py

from faker import Faker

fake = Faker('pl_PL')

print("=== 10 losowych polskich imion i nazwisk ===")
for _ in range(10):
    print(f"  {fake.name()}")

print()
print("=== 10 losowych zdan ===")
for _ in range(10):
    print(f"  {fake.sentence()}")
