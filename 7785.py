import sys

def input(): return sys.stdin.readline().rstrip()

employee = {}

N = int(input())
for _ in range(N):
    data = input().split()

    if data[1] == "enter":
        employee[data[0]] = True
    
    else:
        del employee[data[0]]

for name in sorted(employee, reverse=True):
    print(name)