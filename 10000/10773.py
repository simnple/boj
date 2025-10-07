_ = []

for i in range(int(input())):
    n = int(input())

    if n == 0 and len(_) > 0:
        _.pop()
    
    elif n != 0:
        _.append(n)

print(sum(_))