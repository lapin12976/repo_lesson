number = input("Введите целое положительное число:")
n = 10
f = 1
v = 0
h = 0
d = 0
g = int(len(number))
k = 0
l = int(number)
while g >= 0:
    h = k
    d = l % n
    v = d // f
    f = f * 10
    n = n * 10
    g = g - 1
    if v > h:
        k = v
print(f"Самая большая цифра в вашем числе - {h}")