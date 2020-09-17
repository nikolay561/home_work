from itertools import count, cycle

for el in count(int(input('Введите начальное число: '))):
    if el > 10:
        break
    print(el)

c = 0
for el in cycle('ABC'):
    if c > 10:
        break
    print(el)
    c += 1

