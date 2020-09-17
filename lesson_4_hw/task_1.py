from sys import argv

name, hours, rate_hour, bonus = argv

try:
    result = float(hours) * float(rate_hour) + float(bonus)
    print(f'Заработная плата работника за {hours} часов работы составила {result} рублей.')
except ValueError:
    print('Введите с помощью чисел выработку в часах, ставку в час и бонус: ')
