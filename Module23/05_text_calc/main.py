count = 0
count_line = 0
flag = False
my_list = []
with open('calc.txt','r+') as file:
    try:
        for i in file:

            try:
                count_line += 1
                i_split = i.rstrip().split(' ')
                if len(i_split[1]) != 1 or int(i_split[0])==False or int(i_split[2]) == False:
                    raise BaseException
                else:
                    my_list.append(i)
                    count += (eval(i))
            except BaseException:
                print(f'Обнаружена ошибка в строке: {count_line}')
                flag = True
    finally:
        print('Сумма результатов: ', count)

if flag == True:
    correct = input('Хотите исправить? Y/N: ').lower()
    if correct == 'y':
        new = input('Введите новую строку: ')
        my_list.append(new)

        count1 = 0
        with open('calc.txt','w') as good_file:
            good_file.writelines(my_list)
            for i in my_list:
                count1 += eval(i)
            print('Сумма результатов c исправленной строкой: ', count1)


