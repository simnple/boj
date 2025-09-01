"""
두 개의 정수 A와 B가 주어진다.

A와 B의 크기를 비교하고, A <B이면 -1을, A = B이면 0을, A> B이면 1을 출력하십시오.
"""

A, B = [int(input()) for _ in range(2)]

if A < B:
    print(-1)

elif A == B:
    print(0)

else:
    print(1)