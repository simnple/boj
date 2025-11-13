import sys

input = sys.stdin.readline

N = int(input())
scores = [max(map(int, input().split())) for _ in range(9)]

clubs = ["PROBRAIN", "GROW", "ARGOS", "ADMIN", "ANT", "MOTION", "SPG", "COMON", "ALMIGHTY"]

max_score_club = 0
for i in range(1, 9):
    if scores[max_score_club] < scores[i]:
        max_score_club = i

print(clubs[max_score_club])