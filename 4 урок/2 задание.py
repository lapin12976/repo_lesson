my_list = []
from random import randint
s = randint(5, 20)
while s > 0:
    my_list.append(randint(0, 1000))
    s = s - 1
print(f"Исходный список: {my_list}")

new_list = []
a = 1
b = 0
n = len(my_list) - 1
while n > 0:
    if my_list[a] > my_list[b]:
        new_list.append(my_list[a])
    n = n - 1
    a = a + 1
    b = b + 1
print(f"Результат: {new_list}")

