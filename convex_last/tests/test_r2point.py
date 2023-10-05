from pytest import approx
from math import sqrt
from r2point import R2Point


class TestR2Point:

    # Расстояние от точки до самой себя равно нулю
    def test_dist1(self):
        a = R2Point(1.0, 1.0)
        assert a.dist(R2Point(1.0, 1.0)) == approx(0.0)

    # Расстояние между двумя различными точками положительно
    def test_dist2(self):
        a = R2Point(1.0, 1.0)
        assert a.dist(R2Point(1.0, 0.0)) == approx(1.0)

    def test_dist3(self):
        a = R2Point(1.0, 1.0)
        assert a.dist(R2Point(0.0, 0.0)) == approx(sqrt(2.0))

    # Площадь треугольника равна нулю, если все вершины совпадают
    def test_area1(self):
        a = R2Point(1.0, 1.0)
        assert R2Point.area(a, a, a) == approx(0.0)

    # Площадь треугольника равна нулю, если все вершины лежат на одной прямой
    def test_area2(self):
        a, b, c = R2Point(0.0, 0.0), R2Point(1.0, 1.0), R2Point(2.0, 2.0)
        assert R2Point.area(a, b, c) == approx(0.0)

    # Площадь треугольника положительна при обходе вершин против часовой
    # стрелки
    def test_area3(self):
        a, b, c = R2Point(0.0, 0.0), R2Point(1.0, 0.0), R2Point(1.0, 1.0)
        assert R2Point.area(a, b, c) > 0.0

    # Площадь треугольника отрицательна при обходе вершин по часовой стрелке
    def test_area4(self):
        a, b, c = R2Point(0.0, 0.0), R2Point(1.0, 0.0), R2Point(1.0, 1.0)
        assert R2Point.area(a, c, b) < 0.0

    # Точки могут лежать внутри и вне "стандартного" прямоугольника с
    # противопложными вершинами (0,0) и (2,1)
    def test_is_inside1(self):
        a, b = R2Point(0.0, 0.0), R2Point(2.0, 1.0)
        assert R2Point(1.0, 0.5).is_inside(a, b) is True

    def test_is_inside2(self):
        a, b = R2Point(0.0, 0.0), R2Point(2.0, 1.0)
        assert R2Point(1.0, 0.5).is_inside(b, a) is True

    def test_is_inside3(self):
        a, b = R2Point(0.0, 0.0), R2Point(2.0, 1.0)
        assert R2Point(1.0, 1.5).is_inside(a, b) is False

    # Ребро [(0,0), (1,0)] может быть освещено или нет из определённой точки
    def test_is_light1(self):
        a, b = R2Point(0.0, 0.0), R2Point(1.0, 0.0)
        assert R2Point(0.5, 0.0).is_light(a, b) is False

    def test_is_light2(self):
        a, b = R2Point(0.0, 0.0), R2Point(1.0, 0.0)
        assert R2Point(2.0, 0.0).is_light(a, b) is True

    def test_is_light3(self):
        a, b = R2Point(0.0, 0.0), R2Point(1.0, 0.0)
        assert R2Point(0.5, 0.5).is_light(a, b) is False

    def test_is_light4(self):
        a, b = R2Point(0.0, 0.0), R2Point(1.0, 0.0)
        assert R2Point(0.5, -0.5).is_light(a, b) is True

    # Расстояние от точки до прямой вычисляется
    # Точка лежит на прямой
    def test_distance_point_to_line_1(self):
        R2Point.point_1 = R2Point(-1, 0)
        R2Point.point_2 = R2Point(1, 0)
        R2Point.point = R2Point(0, 0)
        assert R2Point.distance_point_to_line(R2Point.point) == 0.0

    # Точка не лежит на прямой
    def test_distance_point_to_line_2(self):
        # Определяем a, b, c
        R2Point.point_1 = R2Point(-1, 0)
        R2Point.point_2 = R2Point(1, 0)
        R2Point.point = R2Point(5, 5)
        assert R2Point.distance_point_to_line(R2Point.point) == 5.0

    # Расстояние от отрезка до заданной прямой вычисляется корректно
    # Отрезок пересекает прямую
    def test_length_1(self):
        R2Point.point_1 = R2Point(-1, 0)
        R2Point.point_2 = R2Point(1, 0)
        R2Point.point_seg_1 = R2Point(0, 1)
        R2Point.point_seg_2 = R2Point(0, -1)
        assert R2Point.length(R2Point.point_seg_1, R2Point.point_seg_2) == 0.0

    # Один из концов отрезка лежит на прямой
    def test_length_2(self):
        R2Point.point_1 = R2Point(0, 0)
        R2Point.point_2 = R2Point(5, 0)
        R2Point.point_seg_1 = R2Point(0, 1)
        R2Point.point_seg_2 = R2Point(0, -1)
        assert R2Point.length(R2Point.point_seg_1, R2Point.point_seg_2) == 0.0

    # Отрезок и прямая не имеют общих точек
    def test_length_3(self):
        R2Point.point_1 = R2Point(1, 1)
        R2Point.point_2 = R2Point(1, 2)
        R2Point.point_seg_1 = R2Point(0, 0)
        R2Point.point_seg_2 = R2Point(0, 1)
        assert R2Point.length(R2Point.point_seg_1, R2Point.point_seg_2) == 1.0
