import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())

is_enter = False
hello_members = set()
hello_member = 0

for _ in range(N):
    member = input()
    if member == "ENTER":
        is_enter = True
        hello_members = set()
    elif is_enter:
        if member not in hello_members:
            hello_member += 1
            hello_members.add(member)

print(hello_member)