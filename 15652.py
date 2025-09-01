N, M = map(int, input().split())

def sequence(seq):
    if seq:
        if len(seq) < M:
            [sequence(seq + [i]) for i in range(seq[-1], N+1)]

        else:
            print(" ".join(list(map(str, seq))))

    else:
        [sequence([i]) for i in range(1, N+1)]

sequence([])