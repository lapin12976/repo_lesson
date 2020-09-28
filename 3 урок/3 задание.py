def my_func():
    global sum
    a = int(input("Введите первый аргумент:"))
    b = int(input("Введите второй аргумент:"))
    c = int(input("Введите третий аргумент:"))
    list = [a, b, c]
    f = list.index(min(list))
    list.pop(f)
    sum = sum(list)
    return sum
print(my_func())