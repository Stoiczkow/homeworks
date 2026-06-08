from faker import Faker

fake = Faker('pl_PL')

for _ in range(10):
    print(fake.name())
for _ in range(10):
    print(fake.sentence())