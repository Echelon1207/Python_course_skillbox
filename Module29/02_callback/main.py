import functools

app=dict()

def callback(_func=None,*,route):
    def decorator(func):
        app[route] = func

        @functools.wraps(func)
        def wrapped_func(*args,**kwargs):
            res = func(*args,**kwargs)
            return res
        return wrapped_func
    if _func is None:
        return decorator
    return decorator(_func)


@callback(route='//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'

route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')


