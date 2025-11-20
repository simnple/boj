from collections import deque
import sys

input = sys.stdin.readline

def DSLR(cur_num):
    D = (cur_num * 2) % 10_000

    S = cur_num - 1
    if S == -1: S = 9999

    d1, d2 = divmod(cur_num, 1000)
    d2, d3 = divmod(d2, 100)
    d3, d4 = divmod(d3, 10)
    L = d2 * 1000 + d3 * 100 + d4 * 10 + d1
    R = d4 * 1000 + d1 * 100 + d2 * 10 + d3

    return (D, S, L, R)

keywords = ["D", "S", "L", "R"]
T = int(input())

for _ in range(T):
    A, B = map(int, input().split())

    queue = deque([A])
    visited = [""] * 10_000

    while queue and not visited[B]:
        num = queue.popleft()

        for i, n in enumerate(DSLR(num)):
            if not (visited[n] or n == A):
                visited[n] = visited[num] + keywords[i]
                queue.append(n)

    print(visited[B])