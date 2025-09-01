exchange = 5000

for _ in input().split():
    if _ == "1": exchange -= 500
    if _ == "2": exchange -= 800
    if _ == "3": exchange -= 1000

print(exchange)