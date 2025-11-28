T = int(input())

for _ in range(T):
    k = int(input())

    result = 0
    for _ in range(k):
        result += 0.5
        result *= 2
    print(int(result))