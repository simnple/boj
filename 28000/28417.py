import sys

input = sys.stdin.readline

N = int(input())

max_score = 0
for _ in range(N):
    scores = list(map(int, input().split()))
    act_scores = sorted(scores[2:])

    max_score = max(max_score, max(scores[:2]) + act_scores[-1] + act_scores[-2])

print(max_score)