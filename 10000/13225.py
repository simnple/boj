_ = [int(input()) for i in range(int(input()))]

for i in _:
    count = 0
    for j in range(1, i+1):
        if i%j == 0:
            count += 1
    
    print(i, count)