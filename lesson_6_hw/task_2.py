class Road:
    _length = None
    _width = None

    def __init__(self, length, width, weight=25, thickness=5):
        self._length = length
        self._width = width
        self.weight = weight
        self.thickness = thickness

    def result(self):
        print(f'Масса асфальта - {(self._length * self._width * self.weight * self.thickness) // 1000} тонн.')


mass = Road(20, 5000)
mass.result()
