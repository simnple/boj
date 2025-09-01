N, K = map(int, input().split())
multi_tap = list(map(int, input().split()))

count = 0
for i in multi_tap:
    if i % 2 == 0:
        count += i // 2
    else:
        count += i // 2 + 1

if count >= N:
    print("YES")
else:
    print("NO")