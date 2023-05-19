def my_zip(*args):
    g = ((a[i], b[i]) for i in range(min(len(a), len(b))))
    #print(*g, sep = '\n')
    return g

a = [{"x": 4}, "b", "z", "d"]
b = (10, {20,}, [30], "z")

print(my_zip(a, b))
