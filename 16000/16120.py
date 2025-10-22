import sys

def input(): return sys.stdin.readline().rstrip()

string = input()
stack = []
idx = 0

while idx < len(string):
    stack.append(string[idx])
    idx += 1

    if stack[-4:] == list("PPAP"):
        del stack[-4:]
        stack.append("P")

print("PPAP" if stack == ["P"] else "NP")