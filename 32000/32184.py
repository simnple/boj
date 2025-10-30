A, B = map(int, input().split())

count = 0

if A % 2 == 0: count += 1
if B % 2 == 1: count += 1
count += (B - A + 1 - count) // 2

print(count)