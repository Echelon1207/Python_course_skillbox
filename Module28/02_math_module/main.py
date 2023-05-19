from abc import ABC
import math


class MyMath(ABC):

    @classmethod
    def circle_len(cls,radius):
        return f'Длина окружности : {2 * math.pi * radius}'

    @classmethod
    def circle_sq(cls,radius):
        return f'Площадь круга {math.pi * (radius**2)}'

    @classmethod
    def cube_vol(cls,side):
        return f'Объем куба {side**3}'

    @classmethod
    def sphere_sq(cls,radius):
        return f'Площадь поверхности сферы {4 * math.pi * radius * 2}'

res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
print(res_1)
print(res_2)

