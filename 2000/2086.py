# s(n) = f(n+2) - 1
# s(b) - s(a) = f(b+2) - f(a+2)

a, b = map(int, input().split())

fibs = [0, 1]
for i in range(2, b+1):
    fibs.append(fibs[i-1] + fibs[i-2])

print((fibs[b+2] - fibs(a+2)) % 1_000_000_000)