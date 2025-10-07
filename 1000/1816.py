N = int(input())

for _ in range(N):
    S = int(input())

    result = "YES"
    for i in range(2, 1_000_000):
        if S % i == 0:
            result = "NO"
            break

    print(result)