import decimal
decimal.getcontext().prec = 10000

a, b = input().split()

print(format(decimal.Decimal(a) ** decimal.Decimal(b), "f"))