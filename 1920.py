import sys

sys.stdin.readline()
A = set(list(map(int, sys.stdin.readline().split())))
sys.stdin.readline()
B = list(map(int, sys.stdin.readline().split()))

for i in B:
    print(int(A & set([i]) != set()))