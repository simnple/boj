n = int(input())
nums = list(map(int, input().split()))

temp_total = 0
totals = []
for i in nums:
    if i > 0:
        temp_total += i

    else:
        if temp_total + i > 0:
            temp_total += i

        else:
            if temp_total:
                totals.append(temp_total)
                temp_total = 0

            totals.append(i)

if temp_total:
    totals.append(temp_total)

print(max(totals))