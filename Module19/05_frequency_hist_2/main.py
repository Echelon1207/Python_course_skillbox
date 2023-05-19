def histogram(text):
    sym_dict = dict()
    inv_dict = dict()

    for sym in text:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1
    print(sym_dict)

    for key,values in sym_dict.items():
        inv_dict.setdefault(values, []).append(key)
    print(inv_dict)

text = input('Введите текст: ').lower()
histogram(text)



