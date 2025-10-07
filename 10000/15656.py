N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

def sequence(seq):
    if seq:
        if len(seq) < M:
            [sequence(seq + [i]) for i in nums]

        else:
            print(" ".join(list(map(str, seq))))

    else:
        [sequence([i]) for i in nums]

sequence([])