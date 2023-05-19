alfavit_en='abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'

with open('text.txt') as file:
    sym_dict = dict()
    len_file = 0
    result = dict()

    for sym in file.read().lower():
        if sym.lower() in alfavit_en:
            if sym in sym_dict:
                sym_dict[sym] += 1
            else:
                sym_dict[sym] = 1
            len_file +=1

    for key,val in sym_dict.items():
        result[key] = round(int(val) / len_file, 3)

    sort_val = sorted(result.values(), reverse=True)
    sort_result = dict()
    for i in sort_val:
        for j in result.keys():
            if result[j] == i:
                sort_result[j] = result[j]

with open('analysis.txt', 'w') as analysis:
    for key,val in sort_result.items():
        analysis.write(f'{key} {val} \n')




