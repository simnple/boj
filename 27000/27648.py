N, M, K = map(int, input().split())

if M + N - 1 > K:
    print("NO")
else:
    print("YES")
    for i in range(N):
        print(*[j for j in range(i + 1, M + i + 1)])