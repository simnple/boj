a, b = map(int, input().split())
c, d = map(int, input().split())

fence = [0] * 101

for i in range(a + 1, b + 1):
    fence[i] = 1

for i in range(c + 1, d + 1):
    fence[i] = 1

print(sum(fence))