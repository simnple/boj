import sys

input = sys.stdin.readline

tiers = {
    "B": 10**4,
    "S": 10**5,
    "G": 10**6,
    "P": 10**7,
    "D": 10**8
}

N = int(input())
difficults = input().split()
clean_difficults = sorted(difficults, key=lambda x: (tiers[x[0]] + 1000 - int(x[1:])))

for i in range(N):
    clean_score = tiers[clean_difficults[i][0]] + 1000 - int(clean_difficults[i][1:])
    original_score = tiers[difficults[i][0]] + 1000 - int(difficults[i][1:])

    if clean_score != original_score:
        print("KO")
        print(clean_difficults[i], difficults[i])
        break

else:
    print("OK")