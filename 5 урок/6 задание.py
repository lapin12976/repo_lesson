# Получился очень замудрёный код, но он работает. Не смог догадаться как написать попороще, буду ждать лекции.
def func(lis_2):
    list_2 = []
    for r in lis_2:
        d = ord(r)
        if 48 <= d <= 57:
            list_2.append(r)
    s = len(list_2)
    nn = 0
    dd = ""
    while s > 0:
        e = dd
        w = list_2[nn]
        dd = e + w
        nn += 1
        s -= 1
    list_3 = []
    list_3.append(dd)
    return list_3

import json
list = []
dict = {}

with open("text_6.txt", "r", encoding="utf-8") as sun:
    for line in sun:
        l = line.split()
        list.append(l)
    sss = len(list)
    u = 0
    list_t = []
    while sss > 0:
        sss -= 1
        lis = list[u]
        u += 1
        t = 3
        e = 0
        oo = 0
        while t >= 0:
            t -= 1

            for rr in lis[e]:
                d = ord(rr)
                if 48 <= d <= 57:
                    list_t.append(func(lis[e]))
                    oo += 1
                    break
            e += 1
        fg = 0

        if oo > 1:
            while oo > 0:
                eer = fg
                list_y = list_t[0]
                er = int(list_y[0])
                fg = er + eer

                oo -= 1
                list_t.pop(0)
        else:
            list_y = list_t[0]
            fg = list_y[0]
            list_t.pop(0)
        q = lis[0]
        dict.update({q[0:-1]: fg})

print(dict)
