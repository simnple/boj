A = list(map(int, input().split()))

largest_A = max(A)

for i in range(14):
    if A[i] == largest_A:
        print(largest_A + 1)
        break
else:
    print(largest_A)