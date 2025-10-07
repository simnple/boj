from collections import deque
import sys

def input(): return sys.stdin.readline().rstrip()

string = [deque(input()), deque()]

M = int(input())
for _ in range(M):
    cmd = input().split()

    if cmd[0] == "L" and string[0]:
        string[1].appendleft(string[0][-1])
        string[0].pop()

    elif cmd[0] == "D" and string[1]:
        string[0].append(string[1][0])
        string[1].popleft()

    elif cmd[0] == "B" and string[0]:
        string[0].pop()

    elif cmd[0] == "P":
        string[0].append(cmd[1])
    
print("".join(string[0]) + "".join(string[1]))