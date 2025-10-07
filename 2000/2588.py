A, B = [int(input()) for i in range(2)]

print(A * (int(str(B)[2:])))
print(A * (int(str(B)[1:2])))
print(A * (int(str(B)[0:1])))
print(A * B)
