my_list = []
my_list_len = int(input('Введите желаемую длинну списка: '))
i = 1
while i <= my_list_len:
    element = input('Введите элемент списка: ')
    my_list.append(element)
    i += 1
print(f'Вот Ваш список: {my_list}')

i = 0
while i < len(my_list) - 1:
    if i == len(my_list):
        if len(my_list) % 2 == 1:
            break
    my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
    i += 2

print(f'А теперь он такой: {my_list}')
