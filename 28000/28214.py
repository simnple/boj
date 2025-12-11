N, K, P = map(int, input().split())
breads = list(map(int, input().split()))

result = 0
for i in range(0, N * K, K):
    if K - sum(breads[i:i+K]) < P:
        result += 1

print(result)