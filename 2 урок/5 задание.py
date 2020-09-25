a = int(input("Введите новый элемент рейтинга:"))
list = [7, 5, 3, 3, 2]
s = len(list) - 1

while s >= 0:
    if list[s] >= a:
        list.insert(s + 1, a)
        break
    if list[s] < a:
        list.insert(0, a)
        break
    s = s - 1

print(list)
# Без insert к сожалению никак не получилось