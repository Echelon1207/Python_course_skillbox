def divisor(n):
    for i in range(2, n+1):
        if n % i == 0:
            print('Наименьший делитель', i)
            break
n = int(input('Введите число'))
divisor(n)

