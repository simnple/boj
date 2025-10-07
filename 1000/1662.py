S = deque(input().replace(")", "").split("(")[::-1])

result = 0

while S:
    result += len(S.popleft())
    if len(S) > 0:
        result *= int(S[0][-1])
        S[0] = S[0][:-1]

print(result)