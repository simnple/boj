import sys

def input(): return sys.stdin.readline().rstrip()

string = list(input())
c4 = list(input())
stack = []

idx = 0
while idx < len(string):
    stack.append(string[idx])
    idx += 1

    if stack[-len(c4):] == c4:
        del stack[-len(c4):]

print("".join(stack) if len(stack) > 0 else "FRULA")
