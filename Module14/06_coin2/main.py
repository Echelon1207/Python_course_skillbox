from math import*
def coordinates(x, y, r):
    if sqrt(x**2 + y**2) <= r:
        print('Монетка где-то рядом')
    else:
        print('Монетки в области нет')
x = float(input('Введите точку Х: '))
y = float(input('Введите точку Y: '))
r = int(input('Введите радиус: '))
coordinates(x, y, r)
