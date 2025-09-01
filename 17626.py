import math

n = int(input())

count = 0
quit = False

if int(math.sqrt(n))**2 == n:
    count = 1
else:
    for i in range(int(math.sqrt(n)), 0, -1):
        ii = i**2
        if quit == True: break
        for j in range(int(math.sqrt(n - ii)), 0, -1):
            jj = j**2
            if quit == True: break
            if ii + jj > n:
                break
            elif ii + jj == n:
                count = 2
                quit = True
                break
            else:
                for k in range(int(math.sqrt(n - ii - jj)), 0, -1):
                    kk = k**2
                    print(ii, jj, kk)
                    if quit == True: break
                    if ii + jj + kk > n:
                        break
                    elif ii + jj + kk == n:
                        count = 3
                        quit = True
                        break
                    else:
                        for l in range(int(math.sqrt(n - ii - jj - kk)), 0, -1):
                            if quit == True: break
                            if ii + jj + kk + l**2 > n:
                                break
                            elif ii + jj + kk + l**2 == n:
                                count = 4
                                quit = True
                                break
print(count)