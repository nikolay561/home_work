class DivisionZero(Exception):
    def __init__(self, txt):
        self.txt = txt


dividend = input('Введите делимое: ')
divider = input('Введите делитель: ')

try:
    dividend = int(dividend)
    divider = int(divider)
    if divider == 0:
        raise DivisionZero('На ноль делить нельзя!')
    result = dividend / divider

except ValueError:
    print('Введите число!')

except DivisionZero as err:
    print(err)

else:
    print(f'Результат - {result}')
