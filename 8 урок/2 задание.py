class math():
    def __init__(self, par_1, par_2):
        if par_2 == 0:
            print('Ошибка! На ноль делить нельзя.')
        else:
            print(f'{par_1} / {par_2} = {par_1 / par_2:.2f}')
par_1 = int(input('Введите делимое:'))
par_2 = int(input('Введите делитель:'))
math(par_1, par_2)
