class Nums:
    def __init__(self,num):
        self.num = num
        self.count = 0
    def __iter__(self):
        return self
    def __next__(self):
        self.count += 1
        if self.count > self.num:
            raise StopIteration
        return self.count**2

n = Nums(10)
for i in n:
    print(i)

print()
def nums_gen(num):
    for i in range(1,num+1):
        yield i**2

num = 10
for i in nums_gen(num):
    print(i)

print()

numbers =(i**2 for i in range(1,num+1))
for i in numbers:
    print(i)