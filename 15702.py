N, M = map(int, input().split())
scores = list(map(int, input().split()))
tester = dict()

for _ in range(M):
    data = input().split()
    score = 0

    for i in range(0, len(data) - 1):
        if data[i+1] == "O":
            score += scores[i]

    tester[int(data[0])] = score

max_tester = sorted(tester, key=lambda x: (-tester[x], x))[0]
print(max_tester, tester[max_tester])