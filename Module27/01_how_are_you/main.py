import functools

def how_are_you(func):

    @functools.wraps(func)
    def wrapped_func(*args,**kwargs):
        question = input('Как дела? ')
        print('А у меня не очень! Ладно, держи свою функцию.')
        res = func(*args,**kwargs)
        return res
    return wrapped_func

@how_are_you
def test():
    print('<Тут что-то происходит...>')

test()
