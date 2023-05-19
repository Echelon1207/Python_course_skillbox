class Person:
    def __init__(self,name,surname,age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def __str__(self):
        return 'Имя-{}, Фамилия-{}, Возраст-{},'.format(self.__name, self.__surname, self.__age)

class Employee(Person):
    def salary_calculation(self):
        return self.salary_calculation
    def __str__(self):
        return super().__str__() + f'Зарплата-{self.salary_calculation()}.'

class Manager(Employee):
    def salary_calculation(self):
        return 13000
class Agent(Employee):
    def salary_calculation(self):
        return 5000 + self.sales_volume()
    def sales_volume(self):
        sales_volume = int(input('Введите объем продаж: '))
        salary = sales_volume * 0.05
        return salary

class Worker(Employee):
    def salary_calculation(self):
        return  100 * self.hours()
    def hours(self):
        hour = int(input('Введите количество отработанных часов: '))
        return hour

manager1 = Manager('Иван',"Федоров",30)
agent1 = Agent('Ольга',"Иванова",25)
worker1 = Worker('Никита',"Смирнов",40)
print(manager1.__str__())
print(agent1.__str__())
print(worker1.__str__())