site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

def search(site, key):
    if key in site:
        return site[key]

    for i in site.values():
        if isinstance(i, dict):
            result = search(i,key)
            if result:
                    break
    else:
        result = None

    return result

key = input('Введите ключ: ')
depth = input('Хотите ввести макс-ую глубину? Y/N ').lower()

if depth == 'n':
    print(search(site, key))
elif depth == 'y':
    num = int(input('Введите глубину: '))
    if num == 1:
        if key in site:
            print(site[key])
        else:
            print(None)
    else:
        print(search(site, key))
else:
    print('Некорректный ввод')