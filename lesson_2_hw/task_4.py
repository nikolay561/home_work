user_str = input('Введите строку: ')
split_user_str = user_str.split(' ')
for x, y in enumerate(split_user_str, 1):
    print(x, y[:10])
    if x == 10:
        break
