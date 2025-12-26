import sys
import re

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    print("Infected!" if re.fullmatch("(A+|BA+|CA+|DA+|EA+|FA+)(F+)(C+)(A|B|C|D|E|F|)", input().rstrip()) else "Good")