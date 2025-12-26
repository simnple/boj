import re

N = int(input())

for _ in range(N):
    print("YES" if re.fullmatch("((100+1+)|01)+", input()) else "NO")