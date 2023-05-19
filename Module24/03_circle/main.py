import math


class Circle:
    def __init__(self,x=0,y=0,r=1):
        self.x = x
        self.y = y
        self.r = r

    def s(self):
        print('Площадь: ', round(math.pi / (self.r**2), 2))

    def p(self):
        print ("Периметр: ", round((2 * math.pi) * self.r, 2))

    def grow(self,k):
        self.r *= k
        print("Радиус круга увеличился в ", k, "раз, и равен ", self.r)

    def is_intersect(self, other):
        if (self.x - other.x) ** 2 + (self.y - other.y) ** 2 <= (self.r + other.r) ** 2:
            return True
        return False

circle1 = Circle(1,1,2)
circle2 = Circle(2,2,4)

circle1.s()
circle1.grow(2)
circle1.p()
circle1.is_intersect(circle2)