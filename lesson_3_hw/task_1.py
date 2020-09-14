def my_func(x, y):
    try:
        result = x / y
        print(result)
    except ZeroDivisionError:
        print('На ноль делить нельзя!')


my_func(x=int(input('Введите делимое число: ')), y=int(input('Введите делитель: ')))
