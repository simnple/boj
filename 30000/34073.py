import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())
string = input().split()

print("DORO ".join(string) + "DORO")