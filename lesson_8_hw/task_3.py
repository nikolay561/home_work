class MyException:
    def __init__(self):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                user_int = int(input('Введите число: '))
                self.my_list.append(user_int)
                print(f'Текущий список: {self.my_list}\n ')
            except:
                print(f"Вводить можно только числа!")
                user_exit = input(f'Нажмите "Enter" для продолжения или "q" для выхода: ').lower()
                if user_exit == 'q' or user_exit == 'й':
                    return f'Вы вышли.'


result = MyException()
print(result.my_input())
