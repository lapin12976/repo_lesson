from collections import Counter
from random import randint

my_list = []
s = randint(5, 20)
while s > 0:
    my_list.append(randint(0, 20))
    s = s - 1
print(f"Исходный список: {my_list}")

new_list = []
cnt = Counter(my_list)
a = cnt.most_common(len(my_list))
f = len(my_list)
n = 0
while f > 0:
    b = a[n]
    v = b[1]  # сколько раз
    g = b[0]  # какое число
    if v == 1:
        new_list.append(g)
    f = f - v
    n = n + 1
print(f"Результат: {new_list}")