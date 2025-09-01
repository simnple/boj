N = int(input())

answer = list(map(int, input().split()))

streak = 0
score = 0

for i in answer:
    if i == 1:
        streak += 1
        score += streak

    else:
        streak = 0

print(score)