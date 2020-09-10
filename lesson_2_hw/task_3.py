# Вариант через список
list_season = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
user_month = int(input('Введите месяц года цифрой: ')) - 1
if list_season[user_month] == 1 or list_season[user_month] == 2 or list_season[user_month] == 12:
    print('Это зима!')
elif list_season[user_month] == 3 or list_season[user_month] == 4 or list_season[user_month] == 5:
    print('Это весна!')
elif list_season[user_month] == 6 or list_season[user_month] == 7 or list_season[user_month] == 8:
    print('Это лето!')
elif list_season[user_month] == 9 or list_season[user_month] == 10 or list_season[user_month] == 11:
    print('Это осень!')

# Вариант через словарь
dict_season = {
    '1': 'Это зима!',
    '2': 'Это зима!',
    '3': 'Это весна!',
    '4': 'Это весна!',
    '5': 'Это весна!',
    '6': 'Это лето!',
    '7': 'Это лето!',
    '8': 'Это лето!',
    '9': 'Это осень!',
    '10': 'Это осень!',
    '11': 'Это осень!',
    '12': 'Это зима!',
}
user_month = input('Введите месяц года цифрой: ')
print(dict_season[user_month])
