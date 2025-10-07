import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())
stairs = [0] + [int(input()) for _ in range(N)]
max_scores = [0] * (N + 1)

for idx in range(1, N + 1):
    if idx == 1:
        max_scores[idx] = stairs[1]
    elif idx == 2:
        max_scores[idx] = max(
            stairs[2] + stairs[1],
            stairs[2]
        )
    else:
        max_scores[idx] = max(
            stairs[idx] + stairs[idx-1] + max_scores[idx-3],
            stairs[idx] + max_scores[idx-2]
            )

print(max_scores[N])