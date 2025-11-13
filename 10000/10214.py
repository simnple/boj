import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    yonsei = korea = 0

    for __ in range(9):
        Y, K = map(int, input().split())
        yonsei += Y
        korea += K
    
    if yonsei == korea:
        print("Draw")
    elif yonsei > korea:
        print("Yonsei")
    else:
        print("Korea")