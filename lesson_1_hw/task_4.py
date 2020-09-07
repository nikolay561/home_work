user_number = input('Введите целое положительное число: ')
user_number = int(user_number + '0')
user_number = user_number // 10
i = user_number % 10
while user_number > 0:
    if user_number % 10 > i:
        i = user_number % 10
    user_number = user_number // 10
print(f'Самая большая цифра в Вашем числе - {i}.')
