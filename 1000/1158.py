from collections import deque
import sys

def input(): return sys.stdin.readline().rstrip()

N, K = map(int, input().split())

humans = deque(i for i in range(1, N+1))
result = []

count = 1
while len(humans) > 0:
    if count == K:
        result.append(humans.popleft())
        count = 0

    else:
        humans.append(humans.popleft())

    count += 1

print(f"<{', '.join(list(map(str, result)))}>")