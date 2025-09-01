words = [list(input()) for _ in range(5)]

result = []
for x in range(15):
    for y in range(5):
        if x >= len(words[y]):
            continue

        result.append(words[y][x])

print("".join(result))