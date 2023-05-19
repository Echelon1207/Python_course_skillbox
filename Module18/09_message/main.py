text = input('Введите текст: ').split()
answer = []
for i in text:
    if i.isalpha() == False:
        punctuation = i[-1]
        word = i[:-1]
        answer += [word[::-1] + punctuation]
    else:
        answer += [i[::-1]]
print(*answer)