words = input('Введите строку: ').split()
max_word = words[0]
for i in words:
    if len(i) > len(max_word):
        max_word = i
print('Самое длинное слово: ',max_word)
print('Длина слова: ', len(max_word))

