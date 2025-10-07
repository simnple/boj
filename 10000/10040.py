N, M = map(int, input().split())

A = [int(input()) for _ in range(N)]
B = [[i + 1, 0] for i in range(N)]

for _ in range(M):
    vote = int(input())

    for i in range(N):
        if A[i] <= vote:
            B[i][1] += 1
            break

print(sorted(B, key=lambda x: -x[1])[0][0])