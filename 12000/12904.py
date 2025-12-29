from collections import deque
import sys

input = sys.stdin.readline

S = list(input().rstrip())
T = deque(list(input().rstrip()))

check_backward = True
while len(T) > len(S):
    if check_backward:
        if T[-1] == "B":
            T.pop()
            check_backward = False
        else:
            T.pop()
    else:
        if T[0] == "B":
            T.popleft()
            check_backward = True
        else:
            T.popleft()

if check_backward:
    print(int(S == list(T)))
else:
    print(int(S == list(T)[::-1]))
