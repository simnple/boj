N = int(input())
MAP = list(input())

count = 0

for i in range(N):
    if MAP[i:i+2] == ["E", "W"]:
        count += 1

print(count)