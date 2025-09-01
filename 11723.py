import sys

def input(): return sys.stdin.readline().rstrip()

S = 0
for i in range(int(input())):
    cmd = input().split()
    if cmd[0] == "add":
        S |= (1 << (int(cmd[1])-1))

    elif cmd[0] == "remove":
        S &= ~(1 << (int(cmd[1])-1))

    elif cmd[0] == "check":
        print(int(bool(S & (1 << (int(cmd[1])-1)))))

    elif cmd[0] == "toggle":
        S ^= (1 << (int(cmd[1])-1))

    elif cmd[0] == "all":
        S = 2 ** 20 - 1

    elif cmd[0] == "empty":
        S = 0