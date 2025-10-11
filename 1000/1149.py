N = int(input())

total_prices = [0, 0, 0]
for _ in range(N):
    prices = list(map(int, input().split()))
    total_prices = [prices[i] + min([total_prices[j] for j in range(3) if i != j]) for i in range(3)]

print(min(total_prices))