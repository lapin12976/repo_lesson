with open("my_file_1.txt", "w", encoding="utf-8") as sun:
    while True:
        a = input("Введите текст, для окончания ввода - оставьте строку пустой:")
        c = len(a)
        if c != 0:
            sun.writelines(f"{a}\n")
        else:
            break