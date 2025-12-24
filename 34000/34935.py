N = int(input())
A = map(int, input().split())

prev_num = next(A)
for i in A:
    if prev_num < i:
        prev_num = i
    else:
        print(0)
        break
else:
    print(1)