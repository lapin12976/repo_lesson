def my_func(x, y):
    f = x
    while y > 1:
        s = f
        f = s * x
        y = y - 1
    a = 1 / f
    return a
x = int(input("Введите положительное число x:"))
y = abs(int(input("Введите отрицательное число y:")))
print(f"{x}  -{y} = {my_func(x, y)}")