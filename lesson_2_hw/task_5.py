rt = [7, 5, 3, 3, 2]
user_element = int(input('Введите число: '))

for i in range(len(rt)):
    if rt[i] == user_element:
        rt.insert(i + 1, user_element)
        break
    elif user_element > rt[0]:
        rt.insert(0, user_element)
        break
    elif user_element < rt[-1]:
        rt.append(user_element)
        break
    elif rt[i] > user_element > rt[i + 1]:
        rt.insert(i + 1, user_element)
        break

print(rt)
