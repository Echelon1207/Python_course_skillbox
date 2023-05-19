word = list(input('Введите слово: '))
if word == word[::-1]:
    print('Палиндром')
else:
    print("Нет")
