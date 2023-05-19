numbers = [3, 0, 6, 2, 10]
new = []
for i in range(len(numbers)):
    print('Эффективность', i+1, 'клетки = ', numbers[i])
    if i > numbers[i]:
        new.append(numbers[i])
print('Неподходящие значения: ', new)
