from functools import reduce


def my_func(x, y):
    return x * y


print(f'Список с четными числами: {[el for el in range(100, 1001) if el % 2 == 0]}')
print(f'Результат произведения элементов списка: {reduce(my_func, [el for el in range(100, 1001) if el % 2 == 0])}')
