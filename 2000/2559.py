N, K = map(int, input().split())
temperature = list(map(int, input().split()))
temperature_total = [0]

for i in range(N):
    temperature_total.append(temperature_total[i] + temperature[i])

max_temperature = None
for i in range(K, N + 1):
    value = temperature_total[i] - temperature_total[i - K]
    if not max_temperature or value > max_temperature:
        max_temperature = value

print(max_temperature)