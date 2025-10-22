A, B = map(int, input().split())

# 홀 시작 -> 홀수자리 A or A-1
# A + 4*n - 2 -> A-1
# A + 4*n -> A

# 짝 시작 -> 홀수자리 1 or 0
# A + 4*n - 3 -> 1
# A + 4*n - 1 -> 0

if A % 2 == 0: # A 짝
    if B % 2 == 0: # B 짝
        if (B-A) // 2 % 2 == 0:
            print(0^B)
        
        else:
            print(1^B)

    else: # B 홀
        if (B-A) // 2 % 2 == 0:
            print(1)
        
        else:
            print(0)

else: # A 홀
    if B % 2 == 0: # B 짝
        if (B-A) // 2 % 2 == 0:
            print(A^B)
        
        else:
            print(A-1^B)

    else: # B 홀
        if (B-A) // 2 % 2 == 0:
            print(A)
        
        else:
            print(A-1)