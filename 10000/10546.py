import sys

input = sys.stdin.readline

N = int(input())

runner = sorted([input().rstrip() for _ in range(N)])
runner_arrive = sorted([input().rstrip() for _ in range(N-1)])

for i in range(N-1):
    if runner[i] != runner_arrive[i]:
        print(runner[i])
        break

else:
    print(runner[-1])