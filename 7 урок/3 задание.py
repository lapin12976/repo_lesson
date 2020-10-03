class cell:
    def __init__(self, cell):
        self.count = cell
    def __add__(self, other):
        return cell(self.count + other.count)
    def __sub__(self, other):
        return cell(self.count - other.count)
    def __mul__(self,other):
        return cell(self.count * other.count)
    def __floordiv__(self, other):
        return cell(self.count // other.count)
    def __truediv__(self, other):
        return cell(self.count / other.count)


    def make_order(self, n_1, n_2):
        ee = ''
        while n_1 >= n_2:
            ee = ee
            eee = ('*' * n_2)
            ee = ee + eee + "\n"
            n_1 = n_1 - n_2
        if n_1 < n_2 and n_1 != 0:
            ee = ee + ('*' * n_1)
        return ee
    def __str__(self):
        return f'{self.count}'
v_1 = 8
v_2 = 3
m_1 = cell(v_1)
m_2 = cell(v_2)
m = cell(v_1)
print(f'Сумма - {m_1 + m_2}')
print(f'Разность - {m_1 - m_2}')
print(f'Произведение - {m_1 * m_2}')
print(f'Целочисленное деление - {m_1 // m_2}')
print(f'Не целочисленное деление - {m_1 / m_2}')
print(m.make_order(v_1, v_2))
# К сожалению с округлением разобраться не получилось