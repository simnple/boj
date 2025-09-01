data = input().replace("+", "|+").replace("-", "|-").split("|")

for i in data:
    if not i: continue
    if i.replace("+", "").replace("-", "").replace("x", "") == "0":
        print("0")
        break
    if i[-1] == "x":
        if i[:-1] == "+":
            print(1)
        elif i[:-1] == "-":
            print(-1)
        elif i[:-1] == "":
            print(1)
        else:
            print(int(i[:-1]))
    else:
        print(0)
    break