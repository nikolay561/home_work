def my_func(x, y):
    result = x ** y
    print(result)


my_func(5, -2)


def my_func_2(x, y):
    c = 1
    while y < 0:
        c *= x
        y += 1
    print(1 / c)


my_func_2(5, -2)
