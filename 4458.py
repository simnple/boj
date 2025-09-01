# a - 97 / z - 122
# A - 65 / Z - 90
# - 32

N = int(input())
for _ in range(N):
    s = input()
    first_char = s[0]
    if 97 <= ord(s[0]) <= 122:
        first_char = chr(ord(s[0]) - 32)
    print(first_char + s[1:])