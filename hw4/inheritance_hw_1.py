'''
## 2.1 Квадрат
сделать класс Square - квадрат, который наследуется от прямоугольника
Класс Point(x: int, y: int)

# прямоугольник создаем на основе двух точек
Класс Rect(p1, p2)

rect = Rect(p1: Point, p2: Point)
p1 = left_bottom -> (1, 1)  # левая нижняя
p2 = right_top -> (4, 5)    # правая верхняя
methods: area, perimeter (можно через property)


class Square(Rect):
    def __init__(self, p1, size):
        # ...

    # добавить метод вычисления диагонали
    
sq = Square(p1, 5)  # Квадрат 5x5
print(sq.area())
print(sq.perimeter())
print(sq.diag())
'''

import math
class Point():
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x},{self.y})"


class Rectangle:
    def __init__(self,p1: Point, p2: Point):
        self.side_a = p1
        self.side_b = p2

    @property
    def perimetr(self):
        return 2 * (abs(self.side_a.y - self.side_b.y) + abs(self.side_a.x - self.side_b.x))

    @property
    def area(self):
        return abs((self.side_a.y - self.side_b.y) * abs(self.side_a.x - self.side_b.x))

    def __repr__(self):
        return f'({self.side_b.x - self.side_a.x},{self.side_b.y - self.side_a.y})'


class Square(Rectangle):
    def __init__(self,p1,size):
        p2 = Point(p1.x + size, p1.y + size)
        Rectangle.__init__(self, p1, p2)
        self.size = size


    def diagonal(self):
        return self.size *2 ** .5


point_1 = Point(1, 2)
point_2 = Point(3, 4)
point_3 = Point(5,6)

print(f"point_1{point_1}")
print(f"point_2{point_2}")

rectangle = Rectangle(point_1, point_2)
print(f"{rectangle = }")
print(f"Площадь прямоугольника: {rectangle.area}")
print(f"Периметр прямоугольника: {rectangle.perimetr}")

sq = Square(point_1, 3)
print(f"{sq = }")
print(f"Площадь прямоугольника: {sq.area}")
print(f"Периметр прямоугольника: {sq.perimetr}")
print(f"Диагональ прямоугольника: {sq.diagonal()}")



