while True:
    try:
        a = int(input("Введите числитель:"))
        b = int(input("Введите знаменатель:"))
        c = a / b
        print(f"{round(c, 3)}")
        break
    except ZeroDivisionError:
        print("Ошибка, на ноль делить нельзя.")
    except ValueError:
        print("Ошибка, переменная должна быть числом.")
