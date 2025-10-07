from collections import deque
import sys

def input(): return sys.stdin.readline().rstrip()

queue = deque()
cmds = [list(map(int, input().split())) for _ in range(int(input()))]

for cmd in cmds:
    if cmd[0] == 1:
        queue.appendleft(cmd[1])

    elif cmd[0] == 2:
        queue.append(cmd[1])
    
    elif cmd[0] == 3:
        if len(queue) > 0:
            n = queue.popleft()
            print(n)

        else:
            print(-1)

    elif cmd[0] == 4:
        if len(queue) > 0:
            n = queue.pop()
            print(n)

        else:
            print(-1)

    elif cmd[0] == 5:
        print(len(queue))

    elif cmd[0] == 6:
        print(int(not queue))

    elif cmd[0] == 7:
        if len(queue) > 0:
            print(queue[0])

        else:
            print(-1)

    elif cmd[0] == 8:
        if len(queue) > 0:
            print(queue[-1])

        else:
            print(-1)
