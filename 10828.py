import sys

stack = []

def push(x):
    stack.append(x)

def pop():
    front()
    if len(stack) != 0:
        stack.pop(0)

def size():
    print(len(stack))

def empty():
    print(1 if len(stack) == 0 else 0)

def front():
    if len(stack) == 0:
        print(-1)
        return

    print(stack[0])

def back():
    if len(stack) == 0:
        print(-1)
        return

    print(stack[len(stack) - 1])

cmds = [sys.stdin.readline().rstrip().split() for i in range(int(sys.stdin.readline()))]

for cmd in cmds:
    if cmd[0] == "push":
        push(cmd[1])
    
    elif cmd[0] == "pop":
        pop()
    
    elif cmd[0] == "size":
        size()
    
    elif cmd[0] == "empty":
        empty()
    
    elif cmd[0] == "front":
        front()

    elif cmd[0] == "back":
        back()
