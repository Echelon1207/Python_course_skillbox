def bad_years(first,last):
    while first < last:
        for i in range(10):
            if 3 == str(first).count(str(i)):
                print(first)
        first += 1
first = int(input('Введите первый год: '))
last = int(input('Введите последний год: '))
bad_years(first,last)
