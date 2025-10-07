dp = {}

n = int(input())
minimum = 10**(n-1)
maximum = 10**n

for i in range(minimum, maximum):
    is_okay = True

    for j in range(0, n):
        num = i//10**j
        if dp.get(num) == None:
            for k in range(2, num):
                if num % k == 0:
                    is_okay = False
                    dp[num] = is_okay
                    break
        
        else:
            is_okay = False
            break

    if is_okay == True: print(i)