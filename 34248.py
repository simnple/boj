import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())
A = list(map(int, input().split()))

stack = []
while A:
    stack.append(A.pop())

    if len(stack) > 1 and stack[-1] + stack[-2] == 3:
        stack.pop()
        stack.pop()

while stack:
    if len(stack) > 2 and stack[-1] + stack[-2] + stack[-3] == 3:
        stack.pop()
        stack.pop()
        stack.pop()
    
    else:
        break

if stack:
    print("No")
else:
    print("Yes")