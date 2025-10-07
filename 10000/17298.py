from collections import deque

N = int(input())
A = list(map(int, input().split()))

ans = [-1] * N
stack = []
for i in range(N):
    while stack and A[stack[-1]] < A[i]:
        idx = stack.pop()
        ans[idx] = A[i]

    stack.append(i)

print(*ans)