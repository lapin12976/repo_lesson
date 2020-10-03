def my_func(a):
    a = a.title()
    return a

while True:
    a = input("Введите предложение строчными буквами:")
    s = len(a) - 2
    ee = 0
    while s > 0:
        q = ord(a[s])
        if q >= 65 and q <= 90 or q >= 1040 and q<= 1071:
            print("Вы ввели прописную букву.")
            ee = 1
            break
        s = s - 1
    if ee == 0:
        print(my_func(a))
        break