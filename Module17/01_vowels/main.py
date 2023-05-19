vowels = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
text = list(input('Введите текст: '))
count = 0
new = []
for i in vowels:
    for j in text:
        if i == j:
            count += 1
            new.append(i)
print('Список гласных букв: ', new)
print('Длина списка: ', count)

