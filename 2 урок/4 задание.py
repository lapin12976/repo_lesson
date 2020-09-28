a = input("Введите строку из нескольких слов, разделённых пробелами:")

q = a.split()
list = []
d = len(q)
p = len(q)
i = 0

while d > 0:
    if len(q[i]) > 10:
        s = q[i]
        s = s[0:10]
        list.append(s)
        d = d - 1
        i = i + 1

    elif len(q[i]) < 10:
        list.append(q[i])
        d = d - 1
        i = i + 1
for position, g in enumerate(list):
    print(position + 1, g)

