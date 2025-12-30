N, B, C = list(map(int, input().split()))
A = list(map(int, input().split()))

result = 0

i = 0
while i < len(A):
    if B > C and i + 2 < len(A) and A[i] and A[i + 1] and A[i + 2]:
        if i + 3 < len(A) and A[i + 3] and A[i + 1] > A[i + 2]:
            amount = min(A[i], A[i + 1] - A[i + 2])
            A[i] -= amount
            A[i + 1] -= amount
            result += amount * (B + C)
        else:
            amount = min(A[i], A[i + 1], A[i + 2])
            A[i] -= amount
            A[i + 1] -= amount
            A[i + 2] -= amount
            result += amount * (B + C + C)

    elif B > C and i + 1 < len(A) and A[i] and A[i + 1]:
        amount = min(A[i], A[i + 1])
        A[i] -= amount
        A[i + 1] -= amount
        result += amount * (B + C)
    
    elif A[i]:
        result += A[i] * B
        A[i] = 0
    
    else:
        i += 1

print(result)