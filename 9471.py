from collections import deque

def solution(m):
    fib = deque([1, 1, 2 % m])

    i = 1
    while True:
        if fib[0] == 0 and fib[1] == 1 and fib[2] == 1:
            return i

        fib.popleft()
        fib.append((fib[0] + fib[1]) % m)

        i += 1

P = int(input())

for _ in range(P):
    N, M = map(int, input().split())

    print(N, solution(M))