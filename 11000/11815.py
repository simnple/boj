import sys

def input(): return sys.stdin.readline().rstrip()

def get_divisor(x):
    count = 0
    for i in range(1, int(x**(1/2))):
        if x % i == 0:
            if i * i == x:
                count += 1
            else:
                count += 2
    return count

N = int(input())
X = list(map(int, input().split()))
result = []

for i in X:
    count = get_divisor(i)
    if count % 2 == 0:
        result.append("0")
    else:
        result.append("1")

print(" ".join(result))