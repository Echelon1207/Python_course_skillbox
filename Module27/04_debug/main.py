import functools

def debug(func):

    @functools.wraps(func)
    def wrapped_func(name,age=None):

        if age == None:
            print(f'Вызывается {func.__name__}({repr(name)})')
        else:
            print(f'Вызывается {func.__name__}{name,age}')
        res = func(name,age=None)
        print(f'{repr(func.__name__)} вернула значение {repr(res)}')
        return res

    return wrapped_func

@debug
def greeting(name, age=None):
    if age :
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)

print(greeting("Том"))
print()
print(greeting("Миша", age=100))
print()
print(greeting(name="Катя", age=16))

