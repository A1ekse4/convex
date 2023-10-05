#!/usr/bin/env -S python3 -B
from r2point import R2Point
from convex import Void
from convex import Figure

f = Void()

print("Введите первую точку прямой:")
R2Point.point_1 = R2Point()
print("Введите вторую точку прямой:")
R2Point.point_2 = R2Point()
print("\n Точки плоскости: \n")
try:
    while True:
        f = f.add(R2Point())
        print(f"S = {f.area()}, P = {f.perimeter()}, L = {f.length()}")
        print()
except (EOFError, KeyboardInterrupt):
    print("\nStop")
