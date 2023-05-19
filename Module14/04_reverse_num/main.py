def reverse_number(s):
    return '.'.join(p[::-1] for p in s.split('.'))

n = reverse_number(input('Введите первое число: '))
k = reverse_number(input('Введите второе число: '))
print('Первое число наоборот', n)
print('Второе число наоборот', k)
print('Cумма: ', float(n) + float(k))

