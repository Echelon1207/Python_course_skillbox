import functools

def decorator_with_args_for_any_decorator(decorator):
    def decorator_maker(*args,**kwargs):
        def wrapped_decor(func):
            print('Декоратор для декоратора')
            return decorator(func,*args,**kwargs)
        return wrapped_decor
    return decorator_maker


@decorator_with_args_for_any_decorator
def decorated_decorator(func, *dec_args, **dec_kwargs):
    @functools.wraps(func)
    def wrapped_func(*args,**kwargs):
        print(f'Переданные арги и кварги в декоратор: {dec_args}{dec_kwargs}')

        return func(*args,**kwargs)
    return wrapped_func

@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text, num) :
    print("Привет,", text, num)


decorated_function("Юзер", 101)