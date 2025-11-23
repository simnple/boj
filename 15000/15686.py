from itertools import combinations
import sys

input = sys.stdin.readline
inf = sys.maxsize

N, M = map(int, input().split())

house = []
chicken = []

for i in range(N):
    row = list(map(int, input().split()))
    
    for j in range(N):
        if row[j] == 1:
            house.append((i, j))
        elif row[j] == 2:
            chicken.append((i, j))

result = inf
for chickens in combinations(chicken, M):
    total_distance = 0

    for r_1, c_1 in house:
        house_to_chicken_distance = inf
        for r_2, c_2 in chickens:
            distance = abs(r_1 - r_2) + abs(c_1 - c_2)
            house_to_chicken_distance = min(house_to_chicken_distance, distance)
        total_distance += house_to_chicken_distance

    result = min(result, total_distance)

print(result)