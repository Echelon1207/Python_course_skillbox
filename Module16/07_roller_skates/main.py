skates = int(input('Кол-во коньков: '))
skates_list = []
for i in range(skates):
    skates_size = int(input('Введите размер коньков: '))
    skates_list.append(skates_size)

people = int(input('Кол-во людей: '))
people_list = []
for i in range(people):
    people_size = int(input('Введите размер ноги: '))
    people_list.append(people_size)

count = 0
for i in skates_list:
    for j in people_list:
        if i == j:
            count += 1

print('Наибольшее кол-во людей, которые могут взять ролики: ', count)