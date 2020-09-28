e = "название"
f = "цена"
g = "количество"
h = "ед"
i = 1

dict1 = {}
list1 = []
list2 = []
list3 = []
list4 = []

while i > 0:
    aa = input("Введите 'Да' если хотите ввести товар.\nЕсли хоките получить аналитику, то введите 'Нет':")
    if aa == "Да" or aa == "да":
        a = input("Введите  название товара:")
        b = int(input("Введите  цену " + a + "а:"))
        c = int(input("Введите  колличество " + a + "ов:"))
        d = input("Введите  единицу измерения:")
        list1.append((a))
        list2.append((b))
        list3.append((c))
        list4.append((d))
    elif aa == "Нет"  or aa == "нет":
        break

dict1.update({e: list1, f: list2, g: list3, h: list4})

print(dict1)