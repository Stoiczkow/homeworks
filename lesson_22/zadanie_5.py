from faker import Faker

fake = Faker('pl_PL')

print("=== 10 polskich imion i nazwisk ===")
for _ in range(10):
    print(fake.name())

print("\n=== 10 losowych zdan ===")
for _ in range(10):
    print(fake.sentence())
