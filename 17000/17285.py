T = input()
key = ord(T[0]) ^ ord("C")

print("".join([chr(ord(s) ^ key) for s in T]))