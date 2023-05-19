import time
import functools

def decorator(func):

    @functools.wraps(func)
    def wrapped_time(*args,**kwargs):
        print('Ждем 10 секунд...')
        time.sleep(10)
        res = func(*args,**kwargs)
        return res
    return wrapped_time

@decorator
def say_hello(word):
    return word

print(say_hello('Hello!'))

