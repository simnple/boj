import sys

def input(): return sys.stdin.readline().rstrip()

S = input()

stack = []
result = []
for i in range(len(S)):
    s = S[i]
    if s == "<" or (s == " " and stack and not stack[-1][0] == "<"):
        stack.append([s])

    elif not stack:
        stack.append([s])

    elif stack[-1][-1] == ">":
        stack.append([s])

    elif stack[-1][0] == " ":
        stack.append([s])

    else:
        stack[-1].append(s)
    
    if len(stack) > 1 or i == len(S) - 1:
        if stack[0][0] == "<" or stack[0][0] == " ":
            result.extend(stack[0])

        else:
            result.extend(stack[0][::-1])

        del stack[0]

print("".join(result))