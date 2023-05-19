count_orders = int(input('Введите количество заказов: '))
order_dict = dict()
for i in range(count_orders):
    print(f'{i + 1} заказ: ')
    order = input().split()
    if order[0] in order_dict:
        if order[1] in order_dict[order[0]]:
            order_dict[order[0]][order[1]] += int(order[2])
        else:
            order_dict[order[0]][order[1]] = order[2]
    else:
        order_dict[order[0]]= dict({order[1]:int(order[2])})
print(sorted(order_dict.items()))
