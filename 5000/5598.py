S = input()

for s in S:
    n = ord(s) - 3
    if n < 65: n += 26
    print(chr(n), end="")