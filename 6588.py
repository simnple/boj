import sys, math

def input(): return sys.stdin.readline().rstrip()

nums = [True for i in range(1000001)]
nums[0] = nums[1] = False

for i in range(2, int(math.sqrt(1000000))+1):
    if nums[i]:
        for j in range(i*i, 1000001, i):
            nums[j] = False

while True:
    x = int(input())
    if x == 0: break

    is_done = False
    for i in range(3, x//2+1, 2):
        if nums[i] and nums[x-i]:
            is_done = True
            print(f"{x} = {i} + {x-i}")
            break

    if not is_done:
        print("Goldbach's conjecture is wrong.")