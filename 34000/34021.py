T = int(input())
for _ in range(T):
    N, M, L = map(int, input().split())
    S = list(map(int, input().split()))

    smallest = M
    for i in range(N):
        if 0 <= S[i] < smallest: smallest = S[i]

    X = max(M - smallest, L)
    print(f"The scoreboard has been frozen with {X} {'minute' if X == 1 else 'minutes'} remaining.")