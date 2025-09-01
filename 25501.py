import sys

def input(): return sys.stdin.readline().rstrip()

def recursion(s, l, r, c):
    if l >= r: return (1, c)
    elif s[l] != s[r]: return (0, c)
    else: return recursion(s, l+1, r-1, c+1)

def is_palindrome(s):
    return recursion(s, 0, len(s)-1, 1)

T = int(input())

for _ in range(T):
    S = input()
    print(*is_palindrome(S))