N = int(input())
a = list(map(int, input().split()))

nums = dict()

result = "YES"
for i in a:
    if nums.get(i) == None:
        nums[i] = 1
    else:
        nums[i] += 1

    if N % 2 == 0:
        if nums[i] > N // 2:
            result = "NO"
            break
    
    else:
        if nums[i] > N // 2 + 1:
            result = "NO"
            break

print(result)