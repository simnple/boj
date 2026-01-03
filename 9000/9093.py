T = int(input())

for _ in range(T):
    result = []
    S = input().split()
    for s in S:
        result.append(s[::-1])
    print(" ".join(result))