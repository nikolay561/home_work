from random import randint

my_list = []
for el in range(10):
    my_list.append(randint(1, 10))
print(my_list)

new_list = [el for el in my_list if my_list.count(el) < 2]
print(new_list)
