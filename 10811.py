N, M = map(int, input().split())

box = [i+1 for i in range(N)]
for _ in range(M):
    i, j = map(int, input().split())
    temp_box = box[i-1:j]
    temp_box.reverse()
    box[i-1:j] = temp_box

print(*box)