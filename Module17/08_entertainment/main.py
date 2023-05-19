sticks = int(input('Кол-во палок: '))
casts = int(input('Кол-во бросков: '))
row = ['I'] * sticks

for i in range(casts):
    print('Бросок', i + 1)
    while True:
        start = int(input('С какого номера сбиты палки? ')) - 1
        if start >= 0 and start <= sticks:
            break
    while True:
        end = int(input('по номер ')) - 1
        if end >= start and end <= sticks:
            break
    for j in range(start, end + 1):
        row[j] = '.'

print('Результат: ', *row, sep='')

