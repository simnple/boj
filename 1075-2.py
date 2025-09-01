N = int(input())
F = int(input())

StartNum = N // 100 * 100

while StartNum % F != 0:
    StartNum += 1

print(str(StartNum)[-2:])