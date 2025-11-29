N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

sum_A = sum(A)
sum_B = sum(B)

for _ in range(K):
    if sum_A >= sum_B:
        sum_A -= A.pop()
    else:
        sum_B -= B.pop()

print(max(sum_A, sum_B))