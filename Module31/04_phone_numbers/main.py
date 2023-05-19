import re

numbers = ['9999999999', '999999-999', '99999x9999']

for val in numbers:
    if re.match(r"[8-9]{1}[0-9]{9}", val) and len(val) == 10:
        print('Все в порядке')
    else:
        print('Не подходит')

