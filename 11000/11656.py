S = input()

result = [S[i:] for i in range(len(S))]

print(*sorted(result), sep="\n")