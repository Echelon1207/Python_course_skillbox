a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]

a.extend(b)
five = a.count(5)
print('Кол-во цифр 5 при первом объединении: ', five)
for i in a:
    if i == 5:
        a.remove(i)
a.extend(c)
three = a.count(3)
print('Кол-во цифр 3 при втором объединении: ', three)

print('Итоговый список: ', a)