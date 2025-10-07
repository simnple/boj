A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A_work_time = A[3] * 3600 + A[4] * 60 + A[5] - (A[0] * 3600 + A[1] * 60 + A[2])
B_work_time = B[3] * 3600 + B[4] * 60 + B[5] - (B[0] * 3600 + B[1] * 60 + B[2])
C_work_time = C[3] * 3600 + C[4] * 60 + C[5] - (C[0] * 3600 + C[1] * 60 + C[2])

print(A_work_time // 3600, A_work_time % 3600 // 60, A_work_time % 3600 % 60)
print(B_work_time // 3600, B_work_time % 3600 // 60, B_work_time % 3600 % 60)
print(C_work_time // 3600, C_work_time % 3600 // 60, C_work_time % 3600 % 60)
