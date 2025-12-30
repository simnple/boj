import sys

input = sys.stdin.readline

N, M = map(int, input().split())
first_multitab = sorted(map(int, input().split()))
second_multitab = sorted(map(int, input().split()))

A_concent = 1
B_concent = 0

while A_concent and first_multitab and second_multitab:
    value = first_multitab.pop()
    A_concent -= 1
    B_concent += value

    while B_concent and second_multitab:
        value = second_multitab.pop()
        B_concent -= 1
        A_concent += value

print(A_concent)