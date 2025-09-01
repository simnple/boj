S = input()

stack = []
is_opened = False
for s in S:
    if s == "-":
        if not is_opened:
            stack.append(s)
            stack.append("(")
            is_opened = True

        else:
            stack.append(")")
            stack.append(s)
            stack.append("(")

    elif s == "+":
        stack.append(s)
    
    else:
        if not stack or not stack[-1] or not type(stack[-1]) == list:
            stack.append([s])

        else:
            stack[-1].append(s)

if is_opened:
    stack.append(")")

result = []

for s in stack:
    if type(s) == list:
        result.append(str(int("".join(s))))
    else:
        result.append(s)

print(eval("".join(result)))