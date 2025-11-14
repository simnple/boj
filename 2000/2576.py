total = 0
minimum = 100

for _ in range(7):
    n = int(input())
    if n % 2 == 1:
        total += n
        minimum = min(minimum, n)

if total == 0: print(-1)
else:
    print(total)
    print(minimum)