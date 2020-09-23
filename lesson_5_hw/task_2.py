with open('text_2.txt', 'r', encoding='utf-8') as user_txt:
    content = user_txt.readlines()
    print(f'Вот что записано в файле: {content}')
    print(f'Всего {len(content)} строки.')
    print(f'Количество слов в каждой строке: ')
    for i in content:
        print(len(i.split()))
