import math

class Point:
    def __init__(self, x=0, y=0):
        """Инициализация точки с координатами x и y."""
        self.x = x
        self.y = y

    def show(self):
        """Отображение координат точки."""
        print(f"Точка с координатами ({self.x}, {self.y})")

    def move(self, dx, dy):
        """Перемещение точки на (dx, dy)."""
        self.x += dx
        self.y += dy

    def dist(self, other):
        """Вычисление расстояния между текущей точкой и другой точкой."""
        if not isinstance(other, Point):
            raise ValueError("Аргумент должен быть экземпляром класса Point")
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

# Пример использования
point1 = Point(3, 4)
point2 = Point(6, 8)

point1.show()  # Вывод: Точка с координатами (3, 4)
point2.show()  # Вывод: Точка с координатами (6, 8)

distance = point1.dist(point2)
print(f"Расстояние между точками: {distance}")  # Вывод: Расстояние между точками: 5.0

point1.move(1, 1)
point1.show()  # Вывод: Точка с координатами (4, 5)
