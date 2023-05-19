count = int(input('Введите количество видеокарт: '))
videocards =[]
new_videocards = []
counter = 0
for i in range(count):
    print(i+1, 'видеокарта: ', end='')
    name = int(input())
    videocards.append(name)
mx = max(videocards)
for i in videocards:
    if i == mx:
        count += 1
    else:
        new_videocards.append(i)
print(videocards)
print(new_videocards)

