import sys
from collections import deque

def input(): return sys.stdin.readline().rstrip()

N = int(input())
deq = deque()

for _ in range(N):
    cmd = input().split()
    
    if cmd[0] == "push_front":
        deq.appendleft(int(cmd[1]))

    elif cmd[0] == "push_back":
        deq.append(int(cmd[1]))

    elif cmd[0] == "pop_front":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
            deq.popleft()

    elif cmd[0] == "pop_back":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1])
            deq.pop()

    elif cmd[0] == "size":
        print(len(deq))

    elif cmd[0] == "empty":
        print(int(len(deq) == 0))

    elif cmd[0] == "front":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])

    elif cmd[0] == "back":
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1])
