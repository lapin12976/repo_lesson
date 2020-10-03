# очень странно переводит слово four
from translate import Translator
translator= Translator(from_lang="en",to_lang="ru")

list = []
list_3 = []
with open("text_4.txt", "r", encoding="utf-8") as sun:
    for line in sun:
        l = line.split()
        list.append(l)
    ii = len(list)
    i = 0
    while ii > 0:
        f = list[i]
        ff = f[0]
        translation = translator.translate(ff)
        list_2 = f
        list_2.pop(0)
        list_2.insert(0, translation)
        join = " ".join(list_2)
        list_3.append(f"{join}\n")
        list_2.clear()
        i += 1
        ii -= 1
with open("my_file_44.txt", "w", encoding="utf-8") as sun_2:
    sun_2.writelines(list_3)
print(list_3)