def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

A, B = map(int, input().split())
C, D = map(int, input().split())

child = A * D + C * B
parent = B * D
gcd_value = gcd(parent, child)

print(child // gcd_value, parent // gcd_value)