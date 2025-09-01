import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())
M = int(input())
S = input()

count = 0
stack = []
for s in S:
    if not stack and s == "I":
        stack.append([])
        stack[-1].append(s)

    elif stack and stack[-1] and (stack[-1][-1] != s):
        stack[-1].append(s)

    elif s == "I":
        stack.append([])
        stack[-1].append(s)

    else:
        stack.append([])

    if stack and len(stack[-1]) % 2 == 1 and len(stack[-1]) >= (N * 2 + 1):
        count += 1

print(count)