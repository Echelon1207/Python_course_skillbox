
import functools

def singleton(cls):
    @functools.wraps(cls)
    def wrapped_singleton(*args,**kwargs):
        if not wrapped_singleton.instance:
            wrapped_singleton.instance = cls(*args,**kwargs)
        return wrapped_singleton.instance

    wrapped_singleton.instance = None
    return wrapped_singleton

@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()


print(id(my_obj))
print(id(my_another_obj))


