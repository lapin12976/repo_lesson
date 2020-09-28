list = []
x = 0
v = 0
while x == 0:
    a = input("Введите элемент списка, для завершения введите 'Break':")
    if a == "Break" or a == "break":
        break
    v = v + 1
    list.append(a)

print("Ваш список:")
print(list)

v = v // 2

h = 0
j = 1
k = 2

while v > 0:

    r = list[j]
    list.insert(h, r)
    list.pop(k)
    v = v - 1
    h = h + 2
    j = j + 2
    k = k + 2

print("Обменяв значения соседних элементов, ваш список стал таким:")
print(list)