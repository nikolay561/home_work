def sum_func():
    result = 0
    var_exit = False
    while not var_exit:
        number = input('Введите число или несколько чисел, нажмите "q" для выхода: ').split()
        var_sum = 0
        for i in range(len(number)):
            if number[i] == 'q' or number[i] == 'Q':
                var_exit = True
                break
            else:
                var_sum += int(number[i])
        result += var_sum
        print(f'Сумма чисел составляет - {result}')


sum_func()
