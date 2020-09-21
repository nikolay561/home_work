try:
    with open('text_5.txt', 'w+', encoding='utf-8') as text:
        user_int = input('Введите цифры через пробел: ')
        text.writelines(user_int)
        result = user_int.split()
        print(sum(map(int, result)))
except IOError:
    print('Ошибка ввода-вывода.')
except ValueError:
    print('Ошибка, необходимо ввести цифры.')
