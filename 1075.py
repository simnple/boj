N = int(input())
F = int(input())

StartNum = N // 100 * 100

for i in range(0, 100):
    if (StartNum + i) % F == 0:
        if len(str(i)) == 1:
            print("0" + str(i))

        else:
            print(i)
        
        break