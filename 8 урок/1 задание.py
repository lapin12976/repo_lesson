class data:
    def __init__(self, par):
        self.par = par.split("-")

    @staticmethod
    def data_1():
        list = []
        if 0 < int(data(n).par[1]) <= 12:
            dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
            d = dict.get(int(data(n).par[1]))

            if 0 < int(data(n).par[0]) <= d:
                list.append(data(n).par[0])
            else:
                print(f"Для данного месяца день выбирается только в диапазоне от 1 до {d}")

            if 0 < int(data(n).par[1]) <= 12:
                list.append(data(n).par[1])
            else:
                print(f"Месяц выбирается только в диапазоне от 1 до {12}")
            if 0 < int(data(n).par[2]) <= 9999:
                list.append(data(n).par[2])
            else:
                print(f"Год выбирается только в диапазоне от 1 до {9999}")
        else:
            print(f"Месяц выбирается только в диапазоне от 1 до {12}")
        return list
    @classmethod
    def data_2(cls):
        ll = data.data_1()
        try:
            return (f'{ll[0]}.{ll[1]}.{ll[2]}')
        except:
            return 'Ошибка!'
n = '30-10-2020'

print(data.data_2())