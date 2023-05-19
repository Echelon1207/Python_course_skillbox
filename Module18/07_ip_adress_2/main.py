ip = input('Введите IP: ')
ipp = ip.split('.')
count1 = 0
count2 = 0
if len(ipp) < 4:
    print('Должно быть 4 числа')
else:
    for i in ipp:
        if i.isdigit():
            if 0 <= int(i) <= 255:
                count1 += 1
            elif int(i) > 255:
                count2 +=1
                print('Число должно быть меньше 255')
        else:
            print('Должны быть только целые числа')
if count1 == 4 and count2 < 1:
    print('Адрес корректен')
