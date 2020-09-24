import time


class TrafficLight:
    __color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        print('Светофор запущен!')
        while True:
            print(TrafficLight.__color[0])
            time.sleep(7)
            print(TrafficLight.__color[1])
            time.sleep(2)
            print(TrafficLight.__color[2])
            time.sleep(5)
            print(TrafficLight.__color[1])
            time.sleep(2)


working_traffic_light = TrafficLight()
working_traffic_light.running()
