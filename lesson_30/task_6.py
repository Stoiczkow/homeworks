import multiprocessing
import math

def calculate_factorial():
    print(math.factorial(10))
    
def potega(liczba, pot):
    print(liczba**pot)
    
if __name__ == "__main__":
    
    proccess = multiprocessing.Process(target=calculate_factorial)

    proccess.start()
    proccess.join()