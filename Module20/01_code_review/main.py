students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def len_and_age(students):
    hobby = []
    surname_len = 0
    for i in students.values():
       hobby.append(i['interests'])
       surname_len += len(i['surname'])
    return hobby , surname_len

pairs = []
for i,val in students.items():
    pairs+=i, val['age']
print(f'Список пар "ID студента — возраст": {pairs}' )


leen = len_and_age(students)[0]
hobbyy =  len_and_age(students)[1]
print(f'Полный список интересов всех студентов: {leen})')
print(f'Общая длина всех фамилий студентов: {hobbyy}')
