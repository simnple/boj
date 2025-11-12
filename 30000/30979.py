T = int(input())
N = int(input())
F = sum(map(int, input().split()))

if T <= F:
    print("Padaeng_i Happy")
else:
    print("Padaeng_i Cry")