a, b = map(int, input().split())
a = max(3, a - 1) // 2
b = max(3, b) // 2

print(b * (b + 1) - a * (a + 1))