a = int(input("Введите сколько километров пробежал спортсмен в первый день:"))
b = int(input("Введите желаемый результат в километрах:"))

i = 1

while a < b:
    a = a / 10 + a
    i = i + 1
print(f"На {i}-й день спортсмен достиг результата — не менее {b} км.")
