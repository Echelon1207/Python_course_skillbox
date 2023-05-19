import functools
import datetime


def logging(func):

    @functools.wraps(func)
    def wrapped_func(*args,**kwargs):
        try:
            res = func(*args,**kwargs)
            print(f'Название - {func.__name__}.\n {func.__doc__}')
            return res

        except Exception as e:
            time = datetime.datetime.now()
            with open('function_errors.log','a',encoding='utf-8') as file:
                file.write(f'Название функции - {func.__name__}. Ошибка - {e}. Дата и время ошибки: {time} \n')

    return wrapped_func

@logging
def print_word(word):
    """
    Функция выводит на экран введенное пользователем слово.
    """
    print(word)
@logging
def zerodiv():
    """
    Функция вызывает исключение ZeroDivisionError
    """
    num = 1 / 0
    return num

word = input('Введите слово: ')
print_word(word)

zerodiv()