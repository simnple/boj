from collections import deque
import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())

for _ in range(N):
    string = [deque(), deque()]
    
    for s in input():
        if s == "<" and string[0]:
            string[1].appendleft(string[0].pop())

        elif s == ">" and string[1]:
            string[0].append(string[1].popleft())

        elif s == "-" and string[0]:
            string[0].pop()

        elif s not in [">", "<", "-"]:
            string[0].append(s)

    print("".join(string[0]) + "".join(string[1]))