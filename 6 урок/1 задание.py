import time
class light:
    def red(self):
        return 'Красный'
    def ellow(self):
        return 'Желтый'
    def gren(self):
        return 'Зеленый'
def lights():
    #tim = time(30)
    while True:
        a = light()
        print(a.red())
        time.sleep(7)
        print(a.ellow())
        time.sleep(3)
        print(a.gren())
        time.sleep(5)
        print(a.ellow())
        time.sleep(3)
    return
print(lights())