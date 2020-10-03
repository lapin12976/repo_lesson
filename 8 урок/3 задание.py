class list:
    def infinity(self):
        list = []
        ii = 1
        while True:
            text = input("Введите числа, для остановки введите Стоп:")
            if text == "stop" or text == "Stop" or text == "стоп" or text == "Стоп":
                return list
            else:
                for i in text:
                    if 48 <= ord(str(i)) <= 57:
                        pass
                    elif ord(str(i)) != 32:
                        ii = 0
                if ii == 1:
                    list.append(text)
                else:
                    print('Ошибка! Вы ввели символ.')
                ii = 1
print(list().infinity())
