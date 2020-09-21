with open('user.txt', 'w', encoding='utf-8') as user_txt:
    text = input('Введите текст: ')
    while text:
        user_txt.writelines(f'{text}\n')
        text = input('Введите текст: ')
        if not text:
            break
