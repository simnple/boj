N = int(input())

for i in range(N, 0, -1):
    if not str(i).replace("7", "").replace("4", ""):
        print(i)
        break