N = int(input())

count = 0
for _ in range(N):
    S = input()
    if max(S.find("OI"), S.find("01")) != -1:
        count += 1

print(count)