from collections import deque

N = int(input())
balloons = deque(map(int, input().split()))
numbers = deque(range(1, N+1))

result = []
while balloons:
    node = balloons.popleft()
    number = numbers.popleft()
    result.append(number)

    balloons.rotate(-(node - 1 if node > 0 else node))
    numbers.rotate(-(node - 1 if node > 0 else node))

print(*result)