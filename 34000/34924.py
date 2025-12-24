import sys

input = sys.stdin.readline

N = int(input())
S = input().rstrip()

idx = 0
words = 0
pauls = ["L", "U", "A", "P"]

while idx < N:
    if not pauls or S[idx] != pauls[-1]:
        words += 1

    else:
        if words % 2 != 0:
            print("NO")
            break
        words = 0
        if pauls: pauls.pop()

    idx += 1

else:
    print("YES" if not pauls and words % 2 == 0 else "NO")