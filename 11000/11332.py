import sys

def input(): return sys.stdin.readline().rstrip()

ONE_SEC_RUNNING = 100_000_000

N = int(input())
for _ in range(N):
    S, N, T, L = map(lambda x: int(x) if x[0] != "O" else x, input().split())

    running_count = 0
    max_running_count = L * ONE_SEC_RUNNING 
    if S == "O(N)":
        running_count = N * T
    
    elif S == "O(2^N)":
        running_count = 2**N * T

    elif S == "O(N!)":
        is_tle = False
        running_count = 1
        for i in range(N, 0, -1):
            running_count *= i
            if running_count > max_running_count:
                print("TLE!")
                is_tle = True
                break
        if is_tle == True: continue
        running_count *= T
    
    elif S == "O(N^2)":
        running_count = N ** 2 * T
    
    elif S == "O(N^3)":
        running_count = N ** 3 * T

    if running_count <= max_running_count:
        print("May Pass.")
    
    else:
        print("TLE!")