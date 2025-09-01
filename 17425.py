import sys

def input(): return sys.stdin.readline().rstrip()

nums = [0] * (1_000_000 + 1)

T = int(input())

for _ in range(T):
    N = int(input())

    result = nums[N]
    if result == 0:
        for i in range(1, N + 1):
            result += N // i * i

    print(result)