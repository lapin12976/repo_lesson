class matrix:
    def __init__(self, parm_1, parm_2):
        self.m_1 = parm_1
        self.m_2 = parm_2
        self.list_sum = []
    def __add__(self):
        d = len(self.m_1)
        n = 0
        while d > 0:
            list_sum_2 = []
            list_sum_2.append(self.m_1[n][0] + self.m_2[n][0])
            list_sum_2.append(self.m_1[n][1] + self.m_2[n][1])
            self.list_sum.append(list_sum_2)
            d -= 1
            n += 1
        return self.list_sum

    def __str__(self):
        for i in range(len(self.list_sum)):
            for j in range(len(self.list_sum[i])):
                print("{:4}".format(self.list_sum[i][j]), end = " ")
            print()
        return


mx = matrix([[1, 2], [3, 2], [4, 3]], [[2, 1], [3, 1], [4, 2]])
f'add - {mx.__add__()}'
try:
    print(f'mx - {mx}')
except TypeError:
    pass

