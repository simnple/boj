S = input()

for s in ["M", "O", "B", "I", "S"]:
    if s not in S:
        print("NO")
        break
else:
    print("YES")