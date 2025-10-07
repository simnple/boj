N, M = map(int, input().split())
stress_delta = list(map(int, input().split()))

count = 0
current_stress = stress_delta[0]
if current_stress < 0: current_stress = 0
if current_stress >= M: count += 1

for i in stress_delta[1:]:
    current_stress = current_stress + i
    if current_stress < 0: current_stress = 0
    if current_stress >= M: count += 1

print(count)