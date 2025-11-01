import sys

input = sys.stdin.readline

N = int(input())

prev_min_value = [0] * 3
prev_max_value = [0] * 3

for _ in range(N):
    min_value = [0] * 3
    max_value = [0] * 3

    datas = list(map(int, input().split()))

    for i in range(3):
        if i == 0:
            min_value[i] = min([
                prev_min_value[i] + datas[i],
                prev_min_value[i + 1] + datas[i]
            ])

            max_value[i] = max([
                prev_max_value[i] + datas[i],
                prev_max_value[i + 1] + datas[i]
            ])

        elif i == 2:
            min_value[i] = min([
                prev_min_value[i] + datas[i],
                prev_min_value[i - 1] + datas[i]
            ])

            max_value[i] = max([
                prev_max_value[i] + datas[i],
                prev_max_value[i - 1] + datas[i]
            ])

        else:
            min_value[i] = min([
                prev_min_value[i] + datas[i],
                prev_min_value[i - 1] + datas[i],
                prev_min_value[i + 1] + datas[i],
            ])

            max_value[i] = max([
                prev_max_value[i] + datas[i],
                prev_max_value[i - 1] + datas[i],
                prev_max_value[i + 1] + datas[i],
            ])

    prev_max_value = max_value.copy()
    prev_min_value = min_value.copy()

print(max(max_value), min(min_value))