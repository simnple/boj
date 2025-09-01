_ = [input() for i in range(8)]

idx = 0
count = 0
start_at = 1

while idx < 8:
    if idx % 2 == 0: start_at = 0
    else: start_at = 1

    for i in range(start_at, 8, 2):
        if _[idx][i] == "F":
            count += 1
    idx += 1

print(count)