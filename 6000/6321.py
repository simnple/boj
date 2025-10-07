n = int(input())
strings = [input() for _ in range(n)]

for i in range(len(strings)):
    print(f"String #{i + 1}")
    result = []
    for s in strings[i]:
        if s != "Z":
            result.append(chr(ord(s) + 1))
        else:
            result.append("A")
    print("".join(result))
    if i < len(strings) - 1:
        print()