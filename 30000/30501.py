N = int(input())
S = [input() for _ in range(N)]

for i in range(N):
    if S[i].find("S") != -1:
        print(S[i])
        break