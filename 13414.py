import sys

def input(): return sys.stdin.readline().rstrip()

K, L = map(int, input().split())

god = dict()
for _ in range(L):
    number = input()
    if number in god:
        del god[number]
    god[number] = True

print("\n".join(list(god.keys())[:K]))