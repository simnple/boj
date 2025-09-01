from decimal import Decimal, getcontext

getcontext().prec = 1001

A, B = map(int, input().split())
print(Decimal(A)/Decimal(B))