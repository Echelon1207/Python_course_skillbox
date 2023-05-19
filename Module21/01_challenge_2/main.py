def numbers(num):
    if num != 0:
        numbers(num - 1)
        print(num)


num = int(input('Введите число: '))
numbers(num)

