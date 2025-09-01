a1, a0 = map(int, input().split())
c1, c2 = map(int, input().split())
n0 = int(input())

print(int(c1 * n0 <= a1 * n0 + a0 <= c2 * n0))