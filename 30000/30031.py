money = {
    136: 1000,
    142: 5000,
    148: 10000,
    154: 50000
}

N = int(input())
total_money = 0

for _ in range(N):
    w, h = map(int, input().split())
    total_money += money[w]

print(total_money)