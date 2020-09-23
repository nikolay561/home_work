russian = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_txt = []
with open('text_4.txt', 'r+', encoding='utf-8') as user_txt:
    for i in user_txt:
        i = i.split(' ', 1)
        new_txt.append(russian[i[0]] + ' ' + i[1])
    print(new_txt)

with open('new_user_txt.txt', 'w', encoding='utf-8') as user_txt:
    user_txt.writelines(new_txt)
