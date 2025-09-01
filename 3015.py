import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())
humans = [int(input()) for _ in range(N)]

ans = 0
stack = []

for i in range(N):
    j = 1
    while stack and j <= len(stack):
        # print("?")
        if humans[stack[-1]] > humans[stack[-j]]:
            print(f"[POP] 오른쪽이 더 크다. {humans[stack[-1]]}, {humans[stack[-j]]}")
            stack.pop(-j)
        else:
            j += 1

    # if stack and humans[i] < humans[stack[-1]]:
    #     stack = [stack[-1]]
    #     print(f"[스택 초기화] {stack}")

    if stack:
        print(f"[COUNT] {len(stack)}, {stack}")
        ans += len(stack)

    print(f"[PUSH] {humans[i]}")
    stack.append(i)

print(ans)