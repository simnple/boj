N = int(input())
cards = {i: 1 for i in map(int, input().split())}
M = int(input())
print(*[cards.get(i, 0) for i in map(int, input().split())])