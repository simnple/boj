swap = {
    1: {"d": "q", "b": "p", "q": "d", "p": "b"},
    2: {"d": "b", "b": "d", "q": "p", "p": "q"}
    }

N, D = map(int, input().split())

for _ in range(N):
    print("".join([swap[D][s] for s in input()]))