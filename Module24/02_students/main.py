class Student:
    def __init__(self, name, num_g, grades):
        self.name = name
        self.num_g = num_g
        self.grades = grades

    def average_score(self):
        if sum(self.grades) == 0:
            return self.grades
        return sum(self.grades) / len(self.grades)
    def __str__(self):
        result = f'{self.name} {self.num_g} {self.average_score()}'
        return result


students = []

for i in range(3):
    print(f'Студент {i + 1}: ')
    name = input('ФИО: ')
    group_n = int(input('номер группы: '))
    grades = list(map(int, input("оценки: ").split()))
    students.append(Student(name, group_n, grades))

sort = sorted(students, key=lambda x: sum(x.grades))
print(*sort, sep='\n')