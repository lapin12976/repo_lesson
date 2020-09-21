with open("my_file_5", "w", encoding="utf-8") as sun:
    i = input("Введите числа разделенные пробелами:")
    sun.write(i)
with open("my_file_5", "r", encoding="utf-8") as sun:
    for line in sun:
        l = line.split()
    a = 0
    n = 0
    f = len(l)
    while f > 0:
        ss = a
        s = float(l[n])
        a = s + ss
        n += 1
        f -= 1
print(a)