class worker:
    class position:
        get_full_name = input('Введите имя и очество сотрудника:')
        get_total_income = int(input('Введите доход с учетом премии:'))
    dict = {"wage": position().get_total_income * 9 / 10, "bonus": position().get_total_income / 10}
    full_name = position().get_full_name.split()
    name = full_name[0]
    surname = full_name[1]
    position  = f'{position().get_full_name} - доход {position().get_total_income}'
    __income = f"Оклад = {dict.get('wage')}, бонус = {dict.get('bonus')}"
print(worker().name)
print(worker().surname)
print(worker().position)
print(worker()._worker__income)