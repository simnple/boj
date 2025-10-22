import math
import sys

N, K = map(int, sys.stdin.readline().split())
print(math.comb(N, K))