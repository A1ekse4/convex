from math import sqrt


class R2Point:
    """ Точка (Point) на плоскости (R2) """

    # Конструктор
    def __init__(self, x=None, y=None):
        if x is None:
            x = float(input("x -> "))
        if y is None:
            y = float(input("y -> "))
        self.x, self.y = x, y

    # Площадь треугольника
    @staticmethod
    def area(a, b, c):
        return 0.5 * ((a.x - c.x) * (b.y - c.y) - (a.y - c.y) * (b.x - c.x))

    # Лежат ли точки на одной прямой?
    @staticmethod
    def is_triangle(a, b, c):
        return R2Point.area(a, b, c) != 0.0

    # Расстояние до другой точки
    def dist(self, other):
        return sqrt((other.x - self.x)**2 + (other.y - self.y)**2)

    def length(seg_1, seg_2):
        # Находим коэффициенты уравнения прямой
        a = R2Point.point_2.y - R2Point.point_1.y
        b = R2Point.point_1.x - R2Point.point_2.x
        c = R2Point.point_2.x * R2Point.point_1.y - \
            R2Point.point_1.x * R2Point.point_2.y

        # Вычисляем расстояние от каждой конечной точки отрезка до прямой
        distance_start = R2Point.distance_point_to_line(seg_1)
        distance_end = R2Point.distance_point_to_line(seg_2)

        # Проверяем, находится ли точка пересечения на отрезке
        start_value = a * seg_1.x + b * seg_1.y + c
        end_value = a * seg_2.x + b * seg_2.y + c
        if start_value * end_value <= 0:
            return 0.0
        else:
            return min(distance_start, distance_end)

    def distance_point_to_line(seg):
        a = R2Point.point_2.y - R2Point.point_1.y
        b = R2Point.point_1.x - R2Point.point_2.x
        c = R2Point.point_2.x * R2Point.point_1.y - \
            R2Point.point_1.x * R2Point.point_2.y
        d = abs(a * seg.x + b * seg.y + c) / sqrt(a ** 2 + b ** 2)
        return d

    # Лежит ли точка внутри "стандартного" прямоугольника?
    def is_inside(self, a, b):
        return (((a.x <= self.x and self.x <= b.x) or
                 (a.x >= self.x and self.x >= b.x)) and
                ((a.y <= self.y and self.y <= b.y) or
                 (a.y >= self.y and self.y >= b.y)))

    # Освещено ли из данной точки ребро (a,b)?
    def is_light(self, a, b):
        s = R2Point.area(a, b, self)
        return s < 0.0 or (s == 0.0 and not self.is_inside(a, b))

    # Совпадает ли точка с другой?
    def __eq__(self, other):
        if isinstance(other, type(self)):
            return self.x == other.x and self.y == other.y
        return False


if __name__ == "__main__":
    x = R2Point(1.0, 1.0)
    print(type(x), x.__dict__)
    print(x.dist(R2Point(1.0, 0.0)))
    a, b, c = R2Point(0.0, 0.0), R2Point(1.0, 0.0), R2Point(1.0, 1.0)
    print(R2Point.area(a, c, b))
