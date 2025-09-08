A = list(map(int, input().split()))
B = list(map(int, input().split()))

a_score = 0
b_score = 0

last_winner = "D"
for i in range(10):
    if A[i] > B[i]:
        a_score += 3
        last_winner = "A"
    elif A[i] < B[i]:
        b_score += 3
        last_winner = "B"
    else:
        a_score += 1
        b_score += 1

print(a_score, b_score)

if a_score > b_score:
    print("A")
elif a_score < b_score:
    print("B")
else:
    print(last_winner)