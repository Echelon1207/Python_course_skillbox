n = int(input('Кол-во человек: '))
k = int(input('Какое число в считалке? '))

res = 0
for i in range(1, n + 1):
    res = (res + k) % i
print('Остался человек под номером ', res + 1)