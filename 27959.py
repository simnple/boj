# 100원 N개 / M원 초코바
# 100*n >= m

N, M = map(int, input().split(" "))
print("Yes" if 100 * N >= M else "No")