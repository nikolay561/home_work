class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f'Результат: {self.quantity * "*"}'

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        return self.quantity - other.quantity if (self.quantity - other.quantity) > 0 else print('Не может быть < 0')

    def __mul__(self, other):
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        return Cell(round(self.quantity // other.quantity))

    def make_order(self, cells):
        row = ''
        for i in range(int(self.quantity / cells)):
            row += f'{"*" * cells}\\n'
        row += f'{"*" * (self.quantity % cells)}'
        return row


cell_1 = Cell(10)
cell_2 = Cell(5)
print(cell_1)
print(cell_2)
print(cell_1 + cell_2)
print(cell_2 - cell_1)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(2))
print(cell_2.make_order(2))
