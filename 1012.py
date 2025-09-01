from collections import deque
import sys

def input(): return sys.stdin.readline().rstrip()

for _ in range(int(input())):
    M, N, K = map(int, input().split())
    pos = [[0 for ____ in range(M)] for ___ in range(N)]

    for __ in range(K):
        X, Y = map(int, input().split())
        pos[Y][X] = 1

    visited = [[False for ____ in range(M)] for ___ in range(N)]

    count = 0
    for y in range(N):
        for x in range(M):
            if visited[y][x] or not pos[y][x]: continue
            stack = deque([(x, y)])

            while stack:
                node_x, node_y = stack.popleft()
                if not (0 <= node_x <= M - 1) or not (0 <= node_y <= N - 1): continue
                if visited[node_y][node_x] or not pos[node_y][node_x]: continue
                visited[node_y][node_x] = True

                stack.append((node_x-1, node_y))
                stack.append((node_x+1, node_y))
                stack.append((node_x, node_y-1))
                stack.append((node_x, node_y+1))

            count += 1
    print(count)
