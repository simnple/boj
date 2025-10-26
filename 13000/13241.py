A, B = map(int, input().split())

gcd, temp = A, B
while temp:
    gcd, temp = temp, gcd % temp

print(A * B // gcd)