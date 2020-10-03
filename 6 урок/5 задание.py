class Stationery:
    title = 'Достаем'
    def draw(self):
        return 'Запуск отрисовки.'
class Pen(Stationery):
    a = f"{Stationery().title} ручку"
class Pencil(Stationery):
    a = f'{Stationery().title} карандаш'
class Handle(Stationery):
    a = f'{Stationery().title} фломастер'
print(Stationery().draw())
print(Pen().a)
print(Pencil().a)
print(Handle().a)