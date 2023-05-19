num_word = int(input('Скалько пар будет? '))
synonym_dict = dict()

for i in range(num_word):
    synonym = input("Введите 2 синонима через дефис: ").split('-')
    synonym_dict[synonym[0]] = [synonym[1]]

word = input('Введите слово: ')

for key,values in synonym_dict.items():
    if word in key:
        print(values)
        break
    elif word in values:
        print(key)
        break
    else:
        print("Такого слова нет.")


