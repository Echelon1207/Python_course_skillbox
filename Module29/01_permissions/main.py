def check_permission(_func = None,*,name):
    user_permissions = ['admin']
    def decorator(func):

        def wrapped_dec(*args,**kwargs):
            try:
                if name in user_permissions:
                    return func(*args,**kwargs)
                else:
                    raise PermissionError
            except PermissionError as per:
                print(f'Ошибка!У пользователя {name} недостаточно прав, чтобы выполнить функцию {func.__name__}')
        return wrapped_dec
    if _func is None:
        return decorator
    return decorator(_func)


@check_permission(name='admin')
def delete_site():
    print('Удаляем сайт')


@check_permission(name='user_1')
def add_comment():
    print('Добавляем комментарий')

delete_site()
add_comment()
