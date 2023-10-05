from pytest import approx
from math import sqrt
from r2point import R2Point
from convex import Point, Segment, Polygon


class TestPoint:

    # Точка находится на прямой
    def test_point_1(self):
        R2Point.point_1 = R2Point(0.0, 0.0)
        R2Point.point_2 = R2Point(0.0, 1.0)
        assert R2Point.distance_point_to_line(R2Point(0.0, 10.0)) == 0.0

    # Точка лежит не на прямой
    def test_point_2(self):
        R2Point.point_1 = R2Point(0.0, 0.0)
        R2Point.point_2 = R2Point(0.0, 1.0)
        assert R2Point.distance_point_to_line(R2Point(5.0, 10.0)) == 5.0

    def test_point_3(self):
        R2Point.point_1 = R2Point(0.0, 0.0)
        R2Point.point_2 = R2Point(0.0, 1.0)
        assert R2Point.distance_point_to_line(R2Point(1.0, 1.0)) == 1.0


class TestSegment:

    def setup_method(self):
        self.f = Segment(R2Point(0.0, 0.0), R2Point(1.0, 0.0))

    # Отрезок пересекается с заданной прямой
    def test_segment_1(self):
        R2Point.point_1 = R2Point(0.0, 0.0)
        R2Point.point_2 = R2Point(0.0, 1.0)
        assert self.f.length() == 0.0

    # Начало отрезка ближе к прямой
    def test_segment_2(self):
        R2Point.point_1 = R2Point(0.0, 1.0)
        R2Point.point_2 = R2Point(1.0, 1.0)
        self.f.add(R2Point(10.0, 0.0))
        assert self.f.length() == 1.0

    # Конец отрезка ближе к прямой
    def test_segment_3(self):
        R2Point.point_1 = R2Point(-1.0, 5.0)
        R2Point.point_2 = R2Point(1.0, 5.0)
        assert R2Point(-10.0, -1.0).length(R2Point(10.0, 0.0)) == 5.0

    # Отрезок параллелен прямой
    def test_segment_4(self):
        R2Point.point_1 = R2Point(1.0, 0.0)
        R2Point.point_2 = R2Point(1.0, 1.0)
        assert R2Point(4.0, 4.0).length(R2Point(4.0, -3.0)) == 3.0


class TestPolygon:

    def setup_method(self):
        R2Point.point_1 = R2Point(5.0, 0.0)
        R2Point.point_2 = R2Point(5.0, 1.0)
        self.f = Polygon(R2Point(0.0, 0.0), R2Point(1.0, 0.0),
                         R2Point(0.0, 1.0))

    def test_polygon_1(self):
        assert self.f.length() == 4.0

    # Добавление более удаленной точки не меняет результат
    def test_polygon_2(self):
        self.f.add(R2Point(-5.0, 0.0))
        assert self.f.length() == 4.0

    # Добавление точки, которая лежит ближе, чем все точки выпуклой /
    # оболочки, изменит результат
    def test_polygon_3(self):
        self.f.add(R2Point(4.0, 4.0))
        assert self.f.length() == 1.0

    # Добавление точки, которая лежит по другую сторону прямой, приводит /
    # к тому, что результат равен нулю
    def test_polygon_4(self):
        self.f.add(R2Point(7.0, -3.0))
        assert self.f.length() == 0.0
