gain = int(input('Введите выручку фирмы: '))
expenses = int(input('Введите издержки фирмы: '))
if gain > expenses:
    worker = int(input('Введите количество работников: '))
    profit = gain - expenses  # расчет прибыли
    worker = profit / worker  # расчет прибыли на одного работника
    profitability = profit / gain  # расчет рентабельности выручки
    print(f'Выручка больше издержек. Имеется прибыль в размере {profit}.'
          f' Рентабельность выручки составляет {profitability:.2f}.'
          f' В расчете на одного работника прибыль составляет {worker:.2f}.')
elif gain < expenses:
    print('Издержки больше выручки. Прибыли нет.')
elif gain == expenses:
    print('Выручка равна издержкам. Вы вышли в ноль.')
