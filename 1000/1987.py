import sys

input = sys.stdin.readline
diffs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

R, C = map(int, input().split())
box = [list(map(lambda x: 1 << (ord(x) - 64), input().rstrip())) for _ in range(R)]

stack = [(0, 0, box[0][0], 1)]
maximum_move = 1

while stack:
    x, y, history, move = stack.pop()

    for dx, dy in diffs:
        node_x, node_y = x + dx, y + dy

        if not (0 <= node_x < C and 0 <= node_y < R): continue
        if box[node_y][node_x] & history != 0: continue

        maximum_move = max(maximum_move, move + 1)

        stack.append((node_x, node_y, history | box[node_y][node_x], move + 1))

print(maximum_move)