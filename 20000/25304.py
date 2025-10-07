total_price = int(input())
price = 0

_ = [list(map(int, input().split())) for i in range(int(input()))]

for d in _:
    price += d[0] * d[1]

print("Yes" if total_price == price else "No")