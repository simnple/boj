# V - 높이
# A - 낮 올라가는 높이
# B - 밤 내려가는 높이

A, B, V = map(int, input().split())

day = (V - B) // (A - B) + ((V - B) % (A - B) > 0)

print(day)