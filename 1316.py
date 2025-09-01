N = int(input())

count = N
for _ in range(N):
    arr = []
    for s in input():
        if s not in arr:
            arr.append(s)
        elif arr[-1] != s:
            count -= 1
            break

print(count)