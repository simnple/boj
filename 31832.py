N = int(input())
S = [input() for _ in range(N)]

result = ""
for s in S:    
    count = {"lower": 0, "upper": 0, "number": 0}
    for w in s:
        if 65 <= ord(w) <= 90:
            count["upper"] += 1
        elif 97 <= ord(w) <= 122:
            count["lower"] += 1
        elif 48 <= ord(w) <= 57:
            count["number"] += 1

    if count["number"] == len(s) or len(s) > 10: continue
    if count["upper"] > count["lower"]: continue

    result = s
    break

print(result)