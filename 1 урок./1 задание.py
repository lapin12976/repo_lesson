name = input("Введите своё имя:")
patronymic = input("Введите своё очество:")
date = int(input("Введите свой год рождания:"))

import datetime
now = datetime.datetime.now()

old = now.year - date

print(f"Здравствуйте {name}{patronymic}, Ваш возвраст - {old}.")