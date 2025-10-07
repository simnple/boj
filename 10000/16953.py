def solve(i, count, maximum):
    if i > maximum: return -1
    elif i == maximum: return count
    else: return max(solve(i*2, count+1, maximum), solve(int(str(i) + "1"), count+1, maximum))

A, B = map(int, input().split())
print(solve(A, 1, B))