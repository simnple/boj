A, B = map(int, input().split())
N = int(input())
bookmark = [int(input()) for _ in range(N)]

min_count = abs(B - A)
for i in range(N):
    move_count = abs(B - bookmark[i]) + 1

    if min_count > move_count:
        min_count = move_count

print(min_count)