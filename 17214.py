data = input().replace("+", "|+").replace("-", "|-").split("|")
temp = []

for i in data:
    if not i: continue
    if i.replace("x", "").replace("+", "").replace("-", "") == "0": continue

    s = int(i.replace("x", "")) // (i.count("x") + 1)
    if s == 1:
        s = "+"
    elif s == -1:
        s = "-"
    elif s > 0:
        s = "+" + str(s)

    if temp:
        temp.append(str(s) + "x" * (i.count("x") + 1))
    else:
        if str(s)[0:1] == "+":
            temp.append(str(s)[1:] + "x" * (i.count("x") + 1))
        else:
            temp.append(str(s) + "x" * (i.count("x") + 1))

if temp:
    print("".join(temp) + "+W")
else:
    print("W")