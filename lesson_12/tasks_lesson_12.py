from dataclasses import dataclass
#6
class InvalidPasswordError(Exception):
    pass

def set_password(password:str | int):
    try:
        if len(password) < 8:
            raise InvalidPasswordError("The password must have at least 8 characters")
    
        return True
    except InvalidPasswordError as e:
        print(f"Error: {e}")

password_1 = set_password("dasd")
print(password_1)


#task 7

class Data:
    def __init__(self, dzien, miesiac, rok):
        self.dzien = dzien
        self.miesiac = miesiac
        self.rok = rok

    @classmethod
    def ze_stringa(cls, string_:str):
        dzien, miesiac, rok = map(int, string_.split('-'))
        return cls(dzien, miesiac, rok)
    
data_1 = Data.ze_stringa("11-11-2011")
print(data_1.dzien, data_1.miesiac, data_1.rok)

#8

while True:
    try:
        number_1 = float(input("Enter first number: "))
        operation = (input("Choose an operation (+, -, *, /): "))
        number_2 = float(input("Enter second number: "))

        match operation:    
            case "+": result = number_1 + number_2
            case "-": result = number_1 - number_2
            case "*": result = number_1 * number_2
            case "/": result = number_1 / number_2
            case _:
                print("Inccorect operation")
                continue   
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except ValueError:
        print("Error: Please enter valid numeric values")
    else:
        print(f"The result is {result}")
    finally:
        print("End of calculations")
    
#9

from dataclasses import dataclass


class BrakSrodkowError(Exception):
    pass


@dataclass
class KontoBankowe:
    _saldo: int

    @property
    def saldo(self):
        return self._saldo

    def wplac(self, kwota: int):
        if kwota < 0:
            raise ValueError("Kwota wpłaty musi być dodatnia!")
        self._saldo += kwota

    def wyplac(self, kwota: int):
        if kwota < 0:
            raise ValueError("Podana kwota wyplaty powinna byc dodatnia")
        if kwota > self._saldo:
            raise BrakSrodkowError("Srodki na koncie sa niewystarczajace")
        self._saldo -= kwota



try:
    kontoBankowe_1 = KontoBankowe(_saldo=3000)

    print(f"Stan konta na początku: {kontoBankowe_1.saldo} zł")

    kontoBankowe_1.wplac(-500)
    print(f"Stan konta po wpłacie: {kontoBankowe_1.saldo} zł")

    kontoBankowe_1.wyplac(1200)
    print(f"Stan konta po wypłacie: {kontoBankowe_1.saldo} zł")

except ValueError as e:
    print(f"Błąd wartości: {e}")
except BrakSrodkowError as e:
    print(f"Błąd: {e}")
except Exception as e:
    print(f"Błąd: {e}")