from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def __init__(self, size, height):
        self.size = size
        self.height = height

    @property
    def expenses(self):
        return str(f'Общий расход ткани на изделие: {round((self.size / 6.5 + 0.5) + (self.height * 2 + 0.3), 2)}')


class Coat(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.result = round((self.size / 6.5 + 0.5), 2)

    def __str__(self):
        return f'Расход ткани для пальто: {self.result}'


class Suit(Clothes):
    def __init__(self, size, height):
        super().__init__(size, height)
        self.result = round((2 * self.height + 0.3), 2)

    def __str__(self):
        return f'Расход ткани для костюма: {self.result}'


coat = Coat(46, 176)
suit = Suit(52, 182)
print(coat)
print(coat.expenses)
print(suit)
print(suit.expenses)
