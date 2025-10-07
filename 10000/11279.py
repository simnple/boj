N = int(input())

nums = []

for i in range(N):
    num = int(input())
    if num == 0:
        print(max(nums) if len(nums) > 0 else 0)
        try: nums.remove(max(nums))
        except: pass
    else:
        nums.append(num)