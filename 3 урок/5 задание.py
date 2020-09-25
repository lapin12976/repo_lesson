def fun():
    d = 0
    while True:
        a = input("Введите в строку числа, разделенные пробелами:").split()
        qq = a.count("q")
        if qq == 0:
            s = len(a) - 1 - qq
            e = 0
            while s >= 0:
                z = a[s]
                p = e
                w = int(z)
                e = w + p
                s = s - 1
            d = d + e
        if qq > 0:

            l = a.index("q")
            a.pop(l)
            t = len(a) - qq
            m = 0
            while t >= 0:
                y = a[t]
                o = m
                u = int(y)
                m = u + o
                t = t - 1

            d = d + m
            break

    return d

print(fun())