from faker import Faker


fake = Faker("pl_PL")

print("Imiona i nazwiska:")
for _ in range(10):
    print(fake.name())

print("\nZdania:")
for _ in range(10):
    print(fake.sentence())
