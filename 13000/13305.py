import sys

input = sys.stdin.readline

N = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))

min_price_city = 0
total_price = 0

for i in range(N - 1):
    if prices[min_price_city] > prices[i]:
        min_price_city = i
    
    total_price += prices[min_price_city] * distances[i]

print(total_price)