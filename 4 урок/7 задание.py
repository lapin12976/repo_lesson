from math import factorial
n = int(input("Введите число:"))

def fact(n):
    yield factorial(n)

for el in fact(n):
    print(f"Факториал от {n} = {el}.")