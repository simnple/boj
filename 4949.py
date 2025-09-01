import sys

def input(): return sys.stdin.readline().rstrip()

while True:
    s = input()
    if s == ".": break

    data = []

    result = "yes"
    for i in s:
        if i == "(" or i == "[":
            data.append(i)
        
        elif i == ")":
            if len(data) > 0:
                if data[-1] != "(":
                    result = "no"
                    break
                else:
                    data.pop()
            else:
                result = "no"
                break

        elif i == "]":
            if len(data) > 0:
                if data[-1] != "[":
                    result = "no"
                    break
                else:
                    data.pop()
            else:
                result = "no"
                break

    if len(data) > 0:
        result = "no"

    print(result)