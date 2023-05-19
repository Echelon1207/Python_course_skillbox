num = int(input('Введите максимальное число: '))
all_nums = set(range(1, num + 1))
while True:
    nums_true = input('Нужное число есть среди вот этих чисел: ')
    if nums_true == 'Помогите!':
        break
    nums_true = set(int(x) for x in nums_true.split())
    answer = input('Ответ Артёма: ')
    if answer == 'Да':
        all_nums &= nums_true
    else:
        all_nums -= nums_true

print('Артём мог загадать следующие числа: ', *all_nums)
