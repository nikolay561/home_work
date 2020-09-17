def my_func(x, y, z):
    c = [x, y, z]
    c.remove(min(c))
    result = sum(c)
    print(result)


my_func(20, 5, 10)
