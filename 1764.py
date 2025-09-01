import sys

N, M = map(int, input().split())

a = set([sys.stdin.readline().rstrip() for i in range(N)])
b = set([sys.stdin.readline().rstrip() for i in range(M)])

result = list(a & b)

result.sort()
print(len(result))
for s in result:
    print(s)