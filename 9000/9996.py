import sys

input = sys.stdin.readline

N = int(input())
pattern = input().rstrip().split("*")

for _ in range(N):
    name = input().rstrip()

    if name.startswith(pattern[0]) and name.endswith(pattern[1]) and sum([len(pattern[i]) for i in range(2)]) <= len(name):
        print("DA")

    else:
        print("NE")