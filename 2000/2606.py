import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())
N2 = int(input())
_ = [list(map(int, input().split())) for i in range(N2)]
_.sort()

infected = set()
infected.add(1)
last_len = len(infected)

for i in range(N2):
    for start, end in _:
        if start in infected:
            infected.add(end)

        elif end in infected:
            infected.add(start)
    
    if len(infected) == last_len:
        break

print(len(infected) - 1)