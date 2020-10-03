
class stok:
    list = []

    def st(self):
        while True:
            dict_st = {}
            while True:

                try:
                    a = int(input("Добавить технику на склад?. Впишите соответствщую цифру. 1 - Да, 2 - Нет:"))
                    break
                except:
                    print('Ошибка! Введите цифру.')
            if a == 1:
                dict = {1: 'А', 2: 'Б', 3: 'В'}
                while True:
                    try:
                        dict_st.update({'склад': (dict.get(int(input(f'Выбирите склад. Впишите соответствщую цифру. 1 - А, 2 - Б, 3 - В:'))))})
                        break
                    except:
                        print('Ошибка! Введите цифру.')
                org()
                dict_st.update(technics().dict_tex)
                while True:
                    try:
                        dict_st.update({'колличество': (int(input(f'Впишите колличество:')))})
                        break
                    except:
                        print('Ошибка! Введите цифру.')
                print(dict_st)
                stok().list.append(dict_st)
                #stok().dict_st.clear()

            elif a == 2:
                print(stok().list)
                break
            elif a != 1 and a != 2:
                print('Введите цифру 1 или 2')


class technics:
    dict_tex = {}
    def auto(self):
        dict = {1: 'Да', 2: 'Нет'}
        while True:
            try:
                technics().dict_tex.update({'автоподача листов': (dict.get(int(input(f'Выбирите нужна ли вам автоподача листов? Впишите соответствщую цифру. 1 - Да, 2 - Нет:'))))})
                break
            except:
                print('Ошибка! Введите цифру.')
        return
    def form(self):
        dict = {1: 'A4', 2: 'A3', 3: 'A1'}
        while True:
            try:
                technics().dict_tex.update({'формат листов': (dict.get(int(input('Выбирите формат листов для печати. Впишите соответствующую цифру. 1 - А4, 2 - А3, 3 - А1:'))))})
                break
            except:
                print('Ошибка! Введите цифру.')
        return
class printer(technics):
    def color(self):
        dict = {1: 'Черный', 2: 'Белый', 3: 'Красный'}
        while True:
            try:
                technics().dict_tex.update({'цвет принтера': (dict.get(int(input('Выбирите цвет принтера. Впишите соответствующую цифру. 1 - Черный, 2 - Белый, 3 - Красный:'))))})
                break
            except:
                print('Ошибка! Введите цифру.')
        return
class scanner(technics):
    def color(self):
        dict = {1: 'Черный', 2: 'Белый', 3: 'Красный'}
        while True:
            try:
                technics().dict_tex.update({'цвет сканера': (dict.get(int(input('Выбирите цвет сканера. Впишите соответствующую цифру. 1 - Черный, 2 - Белый, 3 - Красный:'))))})
                break
            except:
                print('Ошибка! Введите цифру.')
        return
class copier(technics):
    def color(self):
        dict = {1: 'Черный', 2: 'Белый', 3: 'Красный'}
        while True:
            try:
                technics().dict_tex.update({'цвет ксерокса': (dict.get(int(input('Выбирите цвет ксерокса и впишите соответствующую цифру. 1 - Черный, 2 - Белый, 3 - Красный:'))))})
                break
            except:
                print('Ошибка! Введите цифру.')
        return
def org():
    technics().auto()
    technics().form()
    printer().color()
    scanner().color()
    copier().color()
    #print(technics().dict_tex)
stok().st()
