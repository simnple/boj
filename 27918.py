_ = [input() for i in range(int(input()))]

score = {"D": 0, "P": 0}

for winner in _:
    score[winner] += 1

    if abs(score["D"] - score["P"]) > 1:
        break

print(f"{score['D']}:{score['P']}")