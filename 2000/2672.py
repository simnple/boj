N = int(input())

square = []
x_pos = set()

for _ in range(N):
    x_1, y_1, width, height = map(float, input().split())
    x_2, y_2 = x_1 + width, y_1 + height
    square.append([x_1, y_1, x_2, y_2])

    x_pos.add(x_1)
    x_pos.add(x_2)

x_pos = list(sorted(x_pos))

result = 0

for i in range(len(x_pos) - 1):
    curr_x_1, curr_x_2 = x_pos[i], x_pos[i + 1]

    in_area = []
    for j in range(N):
        x_1, y_1, x_2, y_2 = square[j]
        if x_1 <= curr_x_1 < x_2:
            in_area.append([y_1, y_2])
    
    in_area = sorted(in_area, key=lambda pos: pos[0])

    if not in_area:
        continue

    curr_y_1, curr_y_2 = in_area[0]

    for j in range(1, len(in_area)):
        next_y_1, next_y_2 = in_area[j]

        if next_y_1 < curr_y_2:
            curr_y_2 = max(curr_y_2, next_y_2)
        
        else:
            result += (curr_x_2 - curr_x_1) * (curr_y_2 - curr_y_1)
            curr_y_1, curr_y_2 = next_y_1, next_y_2
    
    result += (curr_x_2 - curr_x_1) * (curr_y_2 - curr_y_1)

if int(result) == result:
    print(int(result))
else:
    print(format(result, ".2f"))