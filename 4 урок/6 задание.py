# итератор, генерирующий целые числа, начиная с указанного
print("итератор, генерирующий целые числа, начиная с указанного")
from itertools import count
from itertools import islice

for i in islice(count(7), 10):
    print(i)

# итератор, повторяющий элементы некоторого списка, определенного заранее
print("итератор, повторяющий элементы некоторого списка, определенного заранее")
from itertools import cycle
v = cycle("ABC")
c = 0
while c < 10:
    print(next(v))
    c = c + 1

# объединенное решение count и cycle
print("объединенное решение count и cycle")
from itertools import count
from itertools import islice
from itertools import cycle

v = cycle(count(7))
c = 0
while c < 10:
    print(next(v))
    c = c + 1