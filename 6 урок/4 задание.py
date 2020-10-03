import random
class car:

    dict = {1: 'Красного', 2: 'Синего', 3: 'Желтого', 4: 'Серого', 5: 'Черного'}
    dict2 = {1: 'Kia', 2: 'Lexus', 3: 'Lada', 4: 'BMW', 5: 'Land Rover'}
    dict3 = {1: 'Право', 2: 'Лево'}
    speed = random.randint(35, 70)
    color = dict.get(random.randint(1, 5))
    name = dict2.get(random.randint(1, 5))
    is_police = f'Началась погоня за машиной {name}.'
    direction = dict3.get(random.randint(1, 2))
    def go(self):
        return f'Машина {car().name} {car().color} цвета поехала со скоростью {car().speed} км/ч.'
    def stop(self):
        return f'Машина {car().name} остановилась.'
    def turn(self, direction):
        return f'Машина {car().name} развернулась на {direction}.'
class TownCar(car):
    show_speed = 60
    def speed_WorkCar(self):
        if car().speed > TownCar().show_speed:
            return (f'Вы привысели скорость {TownCar().show_speed} км/ч, {car().is_police}')
        else:
            return (f'Вы движетесь по TownCar, скоростной режим {TownCar().show_speed} км/ч')
class WorkCar:
    show_speed = 40
    def speed_WorkCar(self):
        if car().speed > WorkCar().show_speed:
            return (f'Вы привысели скорость{WorkCar().show_speed} км/ч, {car().is_police}')
        else:
            return (f'Вы движетесь по WorkCar, скоростной режим {WorkCar().show_speed} км/ч')
print(car().go())
print(TownCar().speed_WorkCar())
print(car().turn(car().direction))
print(WorkCar().speed_WorkCar())
print(car().stop())
