second = int(input("Введите время в секундах:"))

hours = second // 3600
minutes = (second - hours * 3600) // 60
seconds = (second - hours * 3600) % 60

hours1 = hours // 10
minutes1 = minutes // 10
seconds1 = seconds // 10

hours2 = hours % 10
minutes2 = minutes % 10
seconds2 = seconds % 10

print(f"{hours1}{hours2}:{minutes1}{minutes2}:{seconds1}{seconds2}")