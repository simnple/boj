A, B = map(int, input().split())
team = [(A + B) // 2, A - (A + B) // 2]
if min(team) < 0 or (A + B) % 2 != 0:
    print(-1)
else:
    print(*sorted(team, reverse=True))