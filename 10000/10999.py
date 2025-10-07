import sys

def input(): return sys.stdin.readline().rstrip()

N, M, K = map(int, input().split())

nums = [0] * N

for i in range(N):
    n = int(input())
    if i == 0: nums[i] = n
    else: nums[i] = n + nums[i-1]

change_nums = {}

for _ in range(M+K):
    _ = list(map(int, input().split()))
    a = _[0]
    b = _[1]
    c = _[2]
    if len(_) > 3: d = _[3]

    if a == 1:
        if change_nums.get(f"{b-1}-{c-1}") == None:
            change_nums[f"{b-1}-{c-1}"] = d
        else:
            change_nums[f"{b-1}-{c-1}"] = change_nums[f"{b-1}-{c-1}"] + d

    else:
        b -= 1
        c -= 1

        if b == 0: result = nums[c]
        else: result = nums[c] - nums[b-1]

        for i in change_nums:
            start, end = map(int, i.split("-"))
            if (b > start and c < end) or b <= end <= c or b <= start <= c:
                if start < b: start = b
                if c < end: end = c

                multiple = end - start + 1
                result = result + change_nums[i] * multiple

        print(result)
