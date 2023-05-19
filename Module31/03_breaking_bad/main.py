import requests
import json

path = requests.get('https://breakingbadapi.com/api/deaths')

if path.status_code == 200:

    my_dict = json.loads(path.text)
    max_deaths = max(my_dict, key=lambda x:x['number_of_deaths'])
    print('Кол-во смертей макс-ое :',max_deaths['number_of_deaths'],'. Эпизод: ', max_deaths['episode'])

    with open('test.json','w') as file:
        json.dump(max_deaths, file,indent=4)
