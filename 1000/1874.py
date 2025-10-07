n = int(input())

_ = [int(input()) for _ in range(n)]

nums = [0]
output = []
current_num = 1

for i in range(n):
    while nums[-1] < _[i]:
        output.append("+")
        nums.append(current_num)
        current_num += 1

    while nums[-1] > _[i]:
        output.append("-")
        nums.pop()

    if nums[-1] == _[i]:
        output.append("-")
        nums.pop()
    
    else:
        output = ["NO"]
        break

for _ in output:
    print(_)