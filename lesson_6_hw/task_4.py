class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} поворачивает направо'

    def turn_left(self):
        return f'{self.name} поворачивает налево'

    def show_speed(self):
        return f'Скорость {self.name} {self.speed} км/ч.'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость {self.name} {self.speed}')

        if self.speed > 40:
            return f'{self.speed}. Превышение скорости.'
        else:
            return f'{self.speed}. Нормальная скорость.'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость {self.name} {self.speed}')

        if self.speed > 60:
            return f'{self.speed}. Превышение скорости.'
        else:
            return f'{self.speed}. Нормальная скорость.'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} полицейская машина.'
        else:
            return f'{self.name} гражданская машина.'


bmw = SportCar(150, 'Black', 'BMW', False)
kia = TownCar(40, 'Red', 'KIA', False)
audi = WorkCar(100, 'White', 'Audi', False)
skoda = PoliceCar(110, 'Blue', 'Skoda', True)
print(audi.show_speed())
print(bmw.show_speed())
print(kia.show_speed())
print(kia.turn_left())
print(f'{audi.turn_left()} и {bmw.stop()}')
print(f'{audi.go()} едет со скоростью {audi.show_speed()}')
print(f'Цвет {bmw.name} {bmw.color}')
print(f'{skoda.name} {skoda.is_police}')
