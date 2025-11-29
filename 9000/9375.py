from collections import defaultdict

T = int(input())

for _ in range(T):
    n = int(input())
    wears = defaultdict(int)

    for _ in range(n):
        name, wear = input().split()
        wears[wear] += 1
    
    result = 1
    for i in wears.values():
        result *= i + 1
    result -= 1

    print(result)