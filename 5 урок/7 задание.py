import json

with open("text_7.txt", "r", encoding="utf-8") as sun:
    dict = {}
    list = []
    list_2 = []
    i = 0
    for line in sun:
        s = line.split()
        d = int(s[2])
        f = int(s[3])
        ss = d - f
        g = s[0]
        dict.update({g: ss})
        if ss > 0:
            list.append(ss)
            i += 1
    list_2.append(dict)
    list_2.append({"average_profit": sum(list) / i})
    print(list_2)
with open("my_file_7.json", "w", encoding="utf-8") as sun:
    json.dump(list_2, sun, ensure_ascii=False)