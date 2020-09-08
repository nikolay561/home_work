time = int(input('Введите время в секундах: '))
hour = time // 3600
minute = (time % 3600) // 60
second = (time % 3600) % 60
print('{0:02}:{1:02}:{2:02}'.format(hour, minute, second))
