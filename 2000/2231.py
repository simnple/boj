# N 분해합 -> N, 각 자리수 합
# M 분해합 -> N?
# ㄴ M을 N의 생성자

# 245 분해합 -> 256
# why? 245 + 2 + 4 + 5
# v = x*100 + y*10 + 2z + x + y

# 13 분해합 -> 17

_ = int(input())
for i in range(_):
    __ = i
    for j in str(i):
        __ += int(j)
    
    if __ == _:
        print(i)
        break

    elif i == _ - 1:
        print(0)
        break