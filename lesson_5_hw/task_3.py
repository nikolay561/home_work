with open('text_3.txt', 'r', encoding='utf-8') as user_txt:
    top = []
    ne_top = []
    workers = user_txt.read().split('\n')
    for i in workers:
        i = i.split()
        if float(i[1]) < 20000:
            ne_top.append(i[0])
        top.append(i[1])
print(f'Оклад меньше 20 000 у следующих работников: {ne_top}.\n'
      f'Средний оклад составил: {sum(map(float, top)) / len(top)}')
