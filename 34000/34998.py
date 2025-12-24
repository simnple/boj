import sys

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    X = int(input())
    S = input().rstrip()

    result = 0
    for i in S.split(" + "):
        if i == "!":
            result = "!"
            break
        else:
            result += int(i)

            if result > 9:
                result = "!"
                break

    print(result)