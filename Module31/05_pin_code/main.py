import itertools

count = 0
for num in itertools.product(range(10), repeat=4):
    count += 1
    print(num)

print('Вариантов: ', count)
