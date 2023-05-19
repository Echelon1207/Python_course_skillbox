text = input('Введите текст: ')
count = 1
res = ''
for i in range(1, len(text)):
    if text[i - 1] == text[i]:
        count += 1
    else:
        res += text[i - 1] + str(count)
        count = 1

if len(text):
    res += text[-1] + str(count)
print(res)
