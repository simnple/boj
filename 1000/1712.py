A, B, C = map(int, input().split())

if B == C: print(-1)
else:
    result = A // (C - B) + 1
    if result <= 0:
        print(-1)
    else:
        print(result)
