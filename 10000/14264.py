import math

L = int(input())

hexagon_scale = 3 * math.sqrt(3) / 2 * (L ** 2)
triangle_1_scale = math.sin(math.pi * (60 / 180)) * (L ** 2) / 2
triangle_2_scale = (hexagon_scale - triangle_1_scale * 2) / 2

print(format(min(triangle_1_scale, triangle_2_scale), ".15f"))
