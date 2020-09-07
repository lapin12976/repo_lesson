proceeds = int(input("Введите значение выручки фирмы:"))
cost = int(input("Введите значение издержек фирмы:"))

a = proceeds - cost
c = a / proceeds
v = a * 100 / proceeds

if proceeds > cost:
    print(f"Прибыль фирмы составила: {a}. Рентабельность выручки: {c:.2f}, в процентном соотношении: {v:.2f}%.")
elif proceeds < cost:
    print(f"Фирма работала в убыток, который составил: {a}")
elif proceeds == cost:
    print("Фирма работала в 0.")