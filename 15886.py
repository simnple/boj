N = int(input())
MAP = list(input())

count = 0

if MAP[-1] == "E":
    count += 1

if MAP[0] == "W":
    count += 1

for i in range(N):
    if MAP[i:i+2] == ["E", "W"]:
        count += 1

print(count)