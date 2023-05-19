import re

text = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

cars = r'\b\w{1}\d{3}\w{2}\d{2,3}\b'
taxi = r'\w{2}\d{3}\d{2,3}'

print(re.findall(cars, text))
print(re.findall(taxi,text))
