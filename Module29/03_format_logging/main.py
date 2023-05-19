import functools
import time
from datetime import datetime


def timer(cls, func, date_format):
    def wrapped(*args, **kwargs):
        format = date_format
        for sym in format:
            if sym.isalpha():
                format = format.replace(sym, '%' + sym)

        print(f"Запускается '{cls.__name__}.{func.__name__}'. Дата и время запуска: {datetime.now().strftime(format)}")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Завершение '{cls.__name__}.{func.__name__}', время работы = {round(end - start, 3)} сек.")
        return result

    return wrapped



def log_methods(date_format):

    def decorate(cls):
        for i in dir(cls):
            if i.startswith('__') is False:
                curr_meth = getattr(cls,i)
                decorated_method = timer(cls,curr_meth,date_format)
                setattr(cls,i,decorated_method)
        return cls
    return decorate
