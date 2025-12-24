import math

w, h = map(int, input().split())
r = int(input())

print(f"{w * h - math.pi * 0.25 * r ** 2:.2f}")