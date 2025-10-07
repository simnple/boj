A, B = input().split()

for j in range(len(A)):
    for i in range(len(B)):
        if B[i] == A[j]:
            for n in range(len(B)):
                if n != i:
                    print("." * j + B[n] + "." * (len(A) - j - 1))
                else:
                    print(A)
            exit()