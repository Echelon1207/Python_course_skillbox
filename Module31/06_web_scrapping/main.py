import requests
import re

path = requests.get('http://www.columbia.edu/~fdc/sample.html')

#Для  любого сайта, где есть такие теги.
#path = requests.get(input('Введите ссылку: '))

print(re.findall(r'<h3.*>(.+)</h3>', path.text))
