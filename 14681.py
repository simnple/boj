# 사분면 고르기

"""
입력
첫 줄에는 정수 x가 주어진다. (−1000 ≤ x ≤ 1000; x ≠ 0) 다음 줄에는 정수 y가 주어진다. (−1000 ≤ y ≤ 1000; y ≠ 0)

출력
점 (x, y)의 사분면 번호(1, 2, 3, 4 중 하나)를 출력한다.
"""

x = int(input())
y = int(input())

if x > 0:
    if y > 0:
        print("1")
    
    else:
        print("4")

else:
    if y > 0:
        print("2")
    
    else:
        print("3")