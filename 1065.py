# 한자리일때 -> 다 됨
# 두자리일때 -> 다 됨
# 세자리일때 -> 100 ~ 999

N = int(input())

result = 0
if N < 100:
    result = N

else:
    result += 99

    for i in range(100, N+1):
        a = list(map(int, list(str(i)))) # [첫번째자리, 두번째자리, 세번째자리]
        if a[0] - a[1] == a[1] - a[2]:
            result += 1

print(result)