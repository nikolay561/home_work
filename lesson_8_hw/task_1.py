class MyDate:
    def __init__(self, date):
        self.date = str(date)

    @classmethod
    def integer(cls, date):
        result_date = []

        for i in date.split():
            if i != '-':
                result_date.append(i)

        day = int(result_date[0])
        month = int(result_date[1])
        year = int(result_date[2])

        if MyDate.validation(day, month, year):
            return f'{day:02}.{month:02}.{year:04}'
        else:
            return 'Дата введена неверно'

    @staticmethod
    def validation(day, month, year):
        if 1 <= day <= 31 and 1 <= month <= 12 and year > 0:
            return True
        else:
            return False


print(MyDate.integer('01 - 11 - 2020'))
print(MyDate.integer('01 - 22 - 2020'))
