class compl:
    def __init__(self, x, y):
        x = x
        y = y
    def sum(self):
        z = x + y
        return z
    def multi(self):
        q = x * y
        return q
x = complex(1, 2)
y = complex(1, 2)
a = compl(x, y)
b = compl(x, y)
print(a.sum())
print(a.multi())