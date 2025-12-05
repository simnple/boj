N = int(input())

base = set(["2", "3", "0"])

count = 0
for i in range(2023, min(N + 1, 9992023 + 1)):
    num = str(i)

    if not base.issubset(set(num)): continue
    stack = []

    for s in num:
        if not stack and s == "2":
            stack.append(s)
        elif len(stack) == 1 and s == "0":
            stack.append(s)
        elif len(stack) == 2 and s == "2":
            stack.append(s)
        elif len(stack) == 3 and s == "3":
            count += 1
            break

print(count)