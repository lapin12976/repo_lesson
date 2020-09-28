from abc import ABC, abstractmethod
class wear(ABC):
    def __init__(self, parm_1 = int(input('Введите размер для пальто:')), parm_2 = int(input('Введите рост для костюма:'))):
        self.v = parm_1
        self.h = parm_2
    @abstractmethod
    def size(self):
        pass
class cout(wear):
    @property
    def size(self):
        s = self.v / 6.5 + 0.5
        return s
class suit(wear):
    @property
    def size(self):
        t = 2 * self.h + 0.3
        return t
#we = wear(ABS)

co = cout()
su = suit()
consumption = co.size + su.size
print(f'Общий расход ткани = {consumption :.2f}')
