import sys
with open("my_file_2.txt", "r", encoding="utf-8") as sun:
    lines = 0
    words = 0

    for line in sun:
        words1 = words
        lines += 1
        pos = 'out'
        for letter in line:
            if letter != ' ' and pos == 'out':
                words += 1
                pos = 'in'
            elif letter == ' ':
                pos = 'out'
        print(f"Колличество строк в {lines} строке - {words - words1}")
    print(f"Всего строк:{lines}")