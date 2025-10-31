DEBUG_MODE = False

x = 0
y = 0
spend_time = 0
direction = "RIGHT"

lines = []

def debug_print(s):
    if DEBUG_MODE:
        print(s)

def change_direction(d):
    global direction
    if direction == "LEFT":
        if d == "L": direction = "DOWN"
        else: direction = "UP"

    elif direction == "RIGHT":
        if d == "L": direction = "UP"
        else: direction = "DOWN"

    elif direction == "UP":
        if d == "L": direction = "LEFT"
        else: direction = "RIGHT"

    else:
        if d == "L": direction = "RIGHT"
        else: direction = "LEFT"

def is_valid_move(start, end):
    global lines, direction

    x1, y1 = start
    x2, y2 = end

    minimum_t = -1

    debug_print(f"[DEBUG] lines: {len(lines)}")

    # 몸 체크
    debug_print(f"[DEBUG] start line check")
    for pos1, pos2 in lines:
        debug_print(f"[DEBUG] line check this! pos1: {pos1}, pos2: {pos2}")

        t_x1, t_y1 = pos1
        t_x2, t_y2 = pos2

        debug_print(f"[DEBUG] line check condition, first: {min(t_y1, t_y2) <= y1 <= max(t_y1, t_y2)}, second: {min(x1, x2) <= t_x1 <= max(x1, x2) or min(x1, x2) <= t_x2 <= max(x1, x2)}")
        if (direction == "LEFT" or direction == "RIGHT"):
            if (min(t_y1, t_y2) <= y1 <= max(t_y1, t_y2)) and (min(x1, x2) <= t_x1 <= max(x1, x2) or min(x1, x2) <= t_x2 <= max(x1, x2)):
                value = min(abs(t_x1 - x1), abs(t_x2 - x1)) + 1

                debug_print(f"[DEBUG] line check with direction {direction}, value: {value}, pos1: {pos1}, pos2: {pos2}")
                if minimum_t > value or minimum_t == -1:
                    minimum_t = value

        elif (direction == "UP" or direction == "DOWN"):
            if (min(t_x1, t_x2) <= x1 <= max(t_x1, t_x2)) and (min(y1, y2) <= t_y1 <= max(y1, y2) or min(y1, y2) <= t_y2 <= max(y1, y2)):
                value = min(abs(t_y1 - y1), abs(t_y2 - y1)) + 1

                debug_print(f"[DEBUG] line check with direction {direction}, value: {value}, pos1: {pos1}, pos2: {pos2}")
                if minimum_t > value or minimum_t == -1:
                    minimum_t = value

    if minimum_t != -1:
        lines.append([start, end])
        return minimum_t

    # 벽 체크
    debug_print(f"[DEBUG] move info: LEFT_WALL: {-L - 1}, RIGHT_WALL: {L + 1}")
    if (direction == "LEFT" or direction == "RIGHT") and not (-L - 1 < x2 < L + 1):
        if direction == "LEFT": value = abs(-L - 1 - x1) + bool(lines)
        elif direction == "RIGHT": value = abs(L + 1 - x1) + bool(lines)

        if minimum_t > value or minimum_t == -1:
            minimum_t = value
            debug_print(f"[DEBUG] wall check (x), minimum_t: {minimum_t}")

    debug_print(f"[DEBUG] move info: DOWN_WALL: {-L - 1}, UP_WALL: {L + 1}")
    if (direction == "UP" or direction == "DOWN") and not (-L - 1 < y2 < L + 1):
        if direction == "DOWN": value = abs(-L - 1 - y1) + bool(lines)
        elif direction == "UP": value = abs(L + 1 - y1) + bool(lines)

        if minimum_t > value or minimum_t == -1:
            minimum_t = value
            debug_print(f"[DEBUG] wall check (y), minimum_t: {minimum_t}")

    lines.append([start, end])

    return minimum_t

def move_forward(t):
    global x, y, spend_time, lines

    if direction == "LEFT":
        start = (x - 1, y)
        end = (x - t, y)

    elif direction == "RIGHT":
        start = (x + 1, y)
        end = (x + t, y)

    elif direction == "UP":
        start = (x, y + 1)
        end = (x, y + t)

    else:
        start = (x, y - 1)
        end = (x, y - t)

    if not lines: start = (x, y)

    debug_print(f"[DEBUG] move forward, direction: {direction}, start: {start}, end: {end}")

    moved_time = is_valid_move(start, end)

    if moved_time != -1:
        spend_time += moved_time
        return False

    else: moved_time = t

    debug_print(f"[DEBUG] moved time: {moved_time}")

    spend_time += moved_time

    x, y = end
    return True

import sys

input = sys.stdin.readline

L = int(input())
N = int(input())
datas = [input().rstrip().split() for _ in range(N)]

for data in datas:
    t, dir = data
    t = int(t)

    debug_print("")
    debug_print(f"[DEBUG] check input -> ({t}, {dir})")
    if not move_forward(t):
        print(spend_time)
        break
    change_direction(dir)
    debug_print(f"[DEBUG] change direction to {direction}")
    debug_print(f"[DEBUG] spend_time: {spend_time}")

else:
    debug_print("다 통과했는데 살아남았다.")
    move_forward(2*L+1)
    print(spend_time)