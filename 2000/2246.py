import sys

input = sys.stdin.readline

N = int(input())
condo = [tuple(map(int, input().split())) for _ in range(N)]

result = 0
for i in range(N):
    curr_dist, curr_price = condo[i]
    for j in range(N):
        next_dist, next_price = condo[j]
        if curr_dist > next_dist and curr_price >= next_price: break
        if curr_price > next_price and curr_dist >= next_dist: break
    else:
        result += 1

print(result)