T = int(input())

_ = [list(map(int, input().split())) for i in range(T)]

for a,b,c in _:
    count = 0
    for x in range(1, a+1):
        for y in range(1, b+1):
            for z in range(1, c+1):
                if x%y == y%z == z%x:
                    count += 1
    print(count)