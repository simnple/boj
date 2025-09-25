names = [input() for _ in range(5)]
result = [i+1 for i in range(5) if "FBI" in names[i]]

if result:
    print(*result)
else:
    print("HE GOT AWAY!")