S = input()
words = [0] * 26

for s in S:
    words[ord(s) - 97] += 1

print(' '.join(list(map(str, words))))