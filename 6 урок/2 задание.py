class road:
    __length = 5000
    __width = 20
    def form(self, mass, sm):
        d = road()._road__length * road()._road__width * mass * sm // 1000

        return (f'Масса асфальта, необходимого для покрытия всего дорожного полотна равна: {d} тонн.')

a = road()
print(a.form(int(input('Введите массу асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см:')), int(input('Введите число см толщины полотна:'))))
