import sys

data = {0: 0, 1: 1}

def fibonacci(n: int):
    if n == 0:
        return 0
    
    elif n == 1:
        return 1
    
    else:
        if data.get(n) == None:
            data[n] = fibonacci(n-1) + fibonacci(n-2)

        return data[n]

_ = [int(sys.stdin.readline()) for i in range(int(sys.stdin.readline()))]

for i in _:
    fibonacci(i)
    print(data[i-1] if data.get(i-1) != None else 1, data[i])
