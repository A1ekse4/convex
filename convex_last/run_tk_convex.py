#!/usr/bin/env -S python3 -B
from tk_drawer import TkDrawer
from r2point import R2Point
from convex import Void, Point, Segment, Polygon


def void_draw(self, tk):
    pass


def point_draw(self, tk):
    tk.draw_point(self.p)


def segment_draw(self, tk):
    tk.draw_line(self.p, self.q)


def polygon_draw(self, tk):
    for n in range(self.points.size()):
        tk.draw_line(self.points.last(), self.points.first())
        self.points.push_last(self.points.pop_first())


setattr(Void, 'draw', void_draw)
setattr(Point, 'draw', point_draw)
setattr(Segment, 'draw', segment_draw)
setattr(Polygon, 'draw', polygon_draw)


tk = TkDrawer()
f = Void()
tk.clean()

try:
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))
    R2Point.point_1 = R2Point(x1, y1)
    R2Point.point_2 = R2Point(x2, y2)
    xc = 0.0
    xnc = 1.0
    if x1 == x2:
        xc = 1.0
        xnc = 0.0
        k = 1.0
        b = 1.0
    else:
        k = (y2 - y1) / (x2 - x1)
        b = y2 - k * x2
    if xnc == 1:
        tk.draw_line_1(
            R2Point(x1 - 100, k * (x1 - 100) + b), R2Point(
                            x2 + 100, k * (x2 + 100) + b)
        )
    else:
        tk.draw_line_1(R2Point(x1, y1 - 100), R2Point(x2, y2 + 100))
    ans = "0"
    while True:
        f = f.add(R2Point())
        tk.clean()
        f.draw(tk)
        if xnc == 1:
            tk.draw_line_1(
                R2Point(x1 - 100, k * (x1 - 100) + b),
                R2Point(x2 + 100, k * (x2 + 100) + b),
            )
        else:
            tk.draw_line_1(R2Point(x1, y1 - 100), R2Point(x2, y2 + 100))
        print(f"S = {f.area()}, P = {f.perimeter()}, CI = {f.length()}\n")
except (EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()
