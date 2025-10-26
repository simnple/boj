import sys

input = sys.stdin.readline

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

N = int(input())
distance = [int(input()) for _ in range(N)]
distance_diff = distance[1] - distance[0]

for i in range(1, N - 1):
    distance_diff = gcd(distance_diff, distance[i + 1] - distance[i])

print((distance[-1] - distance[0]) // distance_diff - N + 1)
