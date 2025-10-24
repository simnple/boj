N, X = map(int, input().split())
P = sum(map(int, input().split()))

print(int(P % X == 0))