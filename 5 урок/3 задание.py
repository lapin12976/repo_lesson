list = []
list_2 = []

with open("text_3.txt", "r", encoding="utf-8") as sun:
    for line in sun:
        s = line.split()
        list.append(s)
i = 0
d = 0
y = 0
e = len(list)
while e > 0:
    l = list[y]
    c = float(l[1])
    j = d
    if c <= 20000:
        list_2.append(l[0])
    d = c + j
    i += 1
    e -= 1
    y += 1
dd = d / i
print(f"Фамилии работников которые получают оклад менее 20000: {list_2}.\nСредний оклад сотрудников составляет: {dd}.")