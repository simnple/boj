N = int(input())
X = list(map(int, input().split()))
rank = {v: i for i, v in enumerate(sorted(set(X)))}

print(*[rank[i] for i in X])