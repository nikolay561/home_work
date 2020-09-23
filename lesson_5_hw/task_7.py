import json

result = []
company_profit = {}
average_profit = {}
profit = 0
prof_aver = None
i = 0
with open('text_7.txt', 'r', encoding='utf-8') as user_txt:
    for line in user_txt:
        name, form, earning, loss = line.split()
        company_profit[name] = int(earning) - int(loss)
        if company_profit.setdefault(name) >= 0:
            profit += company_profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = profit / i
        print(f'Средняя прибыль: {prof_aver}')
    print(f'Прибыль по каждой компании: {company_profit}')
    average_profit.update({'average_profit': int(prof_aver)})
    result.append(company_profit)
    result.append(average_profit)

with open('text_77.json', 'w', encoding='utf-8') as user_js:
    json.dump(result, user_js)
