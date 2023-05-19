alfavit_en='abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
step = 1
a = []
with open('text.txt') as file:
    for words in file:
        text = ''
        for sym in words.rstrip():
            find_index = alfavit_en.find(sym.lower())
            new_index = find_index + step
            text += alfavit_en[new_index]
        step += 1
        a.append(text)
result = '\n'.join(a)
with open('cipher_text.txt','w') as shifr:
    shifr.write(result)