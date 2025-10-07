N = int(input())
cards = list(map(int, input().split()))

M = int(input())
cards_num = list(map(int, input().split()))
cards_num_copy = cards_num[:]

cards_num.sort()

result = dict()
for i in cards_num:
    result[i] = 0

for i in cards:
    if result.get(i) == None: continue
    start = 0
    end = len(cards_num) - 1

    while start <= end:
        mid = (start + end) // 2

        if cards_num[mid] < i:
            start = mid + 1
        
        elif cards_num[mid] > i:
            end = mid - 1

        else:
            result[i] += 1
            break

print(" ".join(str(result[i]) for i in cards_num_copy))