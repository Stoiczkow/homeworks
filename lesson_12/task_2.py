class User:
    def __init__(self, age):
        self._age = age
        
        @property
        def age(self):
            return self._age

        @age.setter
        def age(self, age):
            if age > 0 and age < 120:
                raise ValueError("Age cannot be negative")
            self._age = age

user = user(20)
print(user.age)