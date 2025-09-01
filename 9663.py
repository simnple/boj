count = 0

def n_queen(x_pos, y_pos):
    global count
    global N

    size = len(x_pos)
    if N == size:
        # print("1")
        count += 1

    elif size == 0:
        for y in range(N):
            for x in range(N):
                n_queen(x_pos + [x], y_pos + [y])

    else:
        for y in range(N):
            if y in y_pos: continue
            for x in range(N):
                if x in x_pos: continue

                need_escape = False
                for i in range(size):
                    for j in range(-N, N+1):
                        if x_pos[i] + j == x and y_pos[i] + j == y:
                            need_escape = True
                            break
                    if need_escape: break
                if need_escape: continue

                n_queen(x_pos + [x], y_pos + [y])

N = int(input())
n_queen([], [])
print(count)