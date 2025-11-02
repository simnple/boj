from collections import deque
import sys

input = sys.stdin.readline

n, d = map(int, input().split())

up_tooth = list(map(int, input().split()))
down_tooth = list(map(int, input().split()))

left_up_tooth = deque(up_tooth)
left_down_tooth = deque(down_tooth)

right_up_tooth = deque(up_tooth)
right_down_tooth = deque(down_tooth)

for i in range(0, n + 1):
    for j in range(n + i):
        if left_up_tooth[j] + left_down_tooth[j] > d:
            break
    else:
        print(i)
        break

    for j in range(n + i):
        if right_up_tooth[j] + right_down_tooth[j] > d:
            break
    else:
        print(i)
        break

    left_up_tooth.appendleft(0)
    left_down_tooth.append(0)

    right_up_tooth.append(0)
    right_down_tooth.appendleft(0)

else:
    print(i)