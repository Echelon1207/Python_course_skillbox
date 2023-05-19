text1 = input('Введите первую строку ')
text2 = input('Введите вторую строку ')
for i in range(len(text1)):
    if text1 == text2:
        print('Строки равны при шаге', i)
        break
    text2 = text2[-1] + text2[:-1]
else:
    print('Нельзя')