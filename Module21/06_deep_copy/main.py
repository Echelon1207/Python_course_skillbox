site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}

def do_site(site,num):
    for i in range(num):
        name = input('Введите название продукта для нового сайта: ')
        site['html']['head']['title']= [f'Куплю/продам {name} недорого']
        site['html']['body']['h2'] = [f'У нас самая низкая цена на {name}']
        print(f'Сайт для {name}: ', site, sep = '\n')

num = int(input('Сколько сайтов: '))
do_site(site,num)

