first_day = int(input('Введите сколько километров Вы пробежали в первый день: '))
finish = int(input('Введите сколько километров вы хотите пробегать за тренировку: '))
result = first_day
days = 1
print(f'{days}-й день: {result}')
while result < finish:
    result = result / 100 * 10 + result
    days = days + 1
    print(f'{days}-й день: {result:.2f}')
print(f'При условий, что Вы будете каждый день увеличивать пезультат на 10%, Вам потребуется {days} дней.')
