import sys

_ = [sys.stdin.readline().rstrip() for i in range(int(sys.stdin.readline()))]

result = ""

for i in range(len(_[0])):
    for s in _:
        if len(result) < i + 1:
            result += s[i]
        
        else:
            if result[i] == "?": break
            elif result[i] != s[i]: result = result[:i] + "?"

print(result)