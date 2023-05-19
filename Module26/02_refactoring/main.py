list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
to_find = 56

def num_gen(to_find,list_1,list_2):
    for x in list_1:
        for y in list_2:
            result = x * y
            print(x, y, result)
            if result == to_find:
                yield True
            yield False

res = num_gen(to_find,list_1,list_2)

for i in res:
    if next(res):
        print('Found!')
        break

