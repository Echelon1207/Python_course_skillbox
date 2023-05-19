def sum_numbers(num):
    count = 0
    while num != 0:
        last = num % 10
        count += last
        num //= 10
    print('Сумма цифр', count)
    return count
def number_of_digits(num):
    count = 0
    while num != 0:
        last = num % 10
        count += 1
        num //= 10
    print('Количество цифр', count)
    return count
num = int(input('Введите число: '))
print('Разность', sum_numbers(num) - number_of_digits(num))
