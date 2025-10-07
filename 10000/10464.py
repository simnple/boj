# 홀 시작 -> 홀수자리 A or A-1
# A + 4*n - 2 -> A-1
# A + 4*n -> A

# 짝 시작 -> 홀수자리 1 or 0
# A + 4*n - 3 -> 1
# A + 4*n - 1 -> 0

T = int(input())

def get_xor(A, B):
    if A % 2 == 0: # A 짝
        if B % 2 == 0: # B 짝
            if (B-A) // 2 % 2 == 0:
                return 0^B
            
            else:
                return 1^B

        else: # B 홀
            if (B-A) // 2 % 2 == 0:
                return 1
            
            else:
                return 0

    else: # A 홀
        if B % 2 == 0: # B 짝
            if (B-A) // 2 % 2 == 0:
                return A^B
            
            else:
                return A-1^B

        else: # B 홀
            if (B-A) // 2 % 2 == 0:
                return A
            
            else:
                return A-1

_ = [list(map(int, input().split())) for i in range(T)]
for S, F in _:
    print(get_xor(S, F))