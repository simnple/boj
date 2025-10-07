import sys

def input(): return sys.stdin.readline().rstrip()

N, M = map(int, input().split())

words = dict()
for _ in range(N):
    word = input()
    if len(word) >= M:
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1

print(*sorted(words, key=lambda x: (-words[x], -len(x), x)), sep="\n")