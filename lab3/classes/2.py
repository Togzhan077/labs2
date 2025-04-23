class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length * self.length

# Пример использования
shape = Shape()
print(f"Площадь Shape: {shape.area()}")  # Вывод: Площадь Shape: 0

square = Square(5)
print(f"Площадь Square: {square.area()}")  # Вывод: Площадь Square: 25