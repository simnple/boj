T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if x1 == x2 and y1 == y2: # 시작이 같을 때
        if r1 == r2: print(-1)
        else: print(0)
    else: # 그 외는 1개 만나거나 2개 만남
        # 1개일땐 서로 만나야함 -> 두 원의 중점을 지나는 직선의 방정식 구하고 그 직선의 방정식과 한 원이 지나는 그 점이 다른 원이 지나는 점이랑 같아야함
        