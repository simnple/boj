S = int(input())

count = 0
total = 0
for i in range(1, S + 1):
    if S - total < i:
        break

    total += i
    count += 1

print(count)