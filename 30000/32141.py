N, H = map(int, input().split())
d = list(map(int, input().split()))

count = 0
for i in d:
    count += 1
    H -= i
    if H <= 0: break

if H > 0: count = -1
print(count)