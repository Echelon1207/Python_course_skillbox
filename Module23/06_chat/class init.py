class Taota:

    def __init__(self,color,price,mx_sp,sp):
        self.color = color
        self.price = price
        self.mx_sp = mx_sp
        self.sp = sp

    def info(self):
        print('{}\n{}\n{}\n{}\n'.format(self.color,self.price,self.mx_sp,self.sp))

car1 = Taota('red',500000,200,0)
car1.info()