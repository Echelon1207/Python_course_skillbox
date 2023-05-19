# TODO здесь писать код
a = []
b = []

numbers = [int(i) for i in range(10)]

for i in numbers:
    if numbers[i] % 2 != 0:
        a.append(i)
    else:
        b.append(i)

my_tuple = zip(b, a)
print(list(my_tuple))