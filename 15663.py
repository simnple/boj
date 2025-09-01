N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

def sequence(seq):
    if seq:
        if len(seq) < M:
            items = [seq + [i] for i in range(0, len(nums)) if i not in seq]
            for i in range(0, len(items)):
                if i > 0 and nums[items[i][-1]] == nums[items[i-1][-1]]: continue
                sequence(items[i])

        else:
            print(" ".join(list(map(lambda x: str(nums[x]), seq))))

    else:
        items = [[i] for i in range(0, len(nums))]
        for i in range(0, len(items)):
            if i > 0 and nums[items[i][-1]] == nums[items[i-1][-1]]: continue
            sequence(items[i])

sequence([])