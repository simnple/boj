from collections import deque
import sys

def input(): return sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    p = input()
    n = int(input())
    x = deque(eval(input()))
    reversed_count = 0

    result = ""
    for s in p:
        if s == "R":
            reversed_count += 1
        else:
            if x:
                if reversed_count % 2 == 1:
                    x.pop()
                else:
                    x.popleft()
            else:
                result = "error"
                break

    if not result: result = "[" + ",".join(list(map(str, x if reversed_count % 2 == 0 else list(x)[::-1]))) + "]"
    print(result)