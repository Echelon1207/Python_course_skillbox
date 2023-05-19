
def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1

        return func(*args, **kwargs)

    wrapper.count = 0
    return wrapper

@counter
def say_hello():
    print("Hello")


say_hello()
say_hello()
say_hello()
print(say_hello.count)
