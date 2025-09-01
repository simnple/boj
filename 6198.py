import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())
H = [int(input()) for _ in range(N)]

ans = 0
stack = []

for i in range(N):
    while stack and H[stack[-1]] <= H[i]:
        stack.pop()
    
    if stack:
        ans += len(stack)

    stack.append(i)

print(ans)