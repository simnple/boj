S = input()

result = set()
for i in range(1, len(S)):
    for j in range(0, len(S)):
        if j >= len(S): break
        result.add(S[j:j+i])

print(len(result) + 1)