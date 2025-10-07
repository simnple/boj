import sys

def input(): return sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    C = int(input())
    
    quarter = C // 25
    dime = C % 25 // 10
    nickel = C % 25 % 10 // 5
    penny = C % 25 % 10 % 5
    
    print(quarter, dime, nickel, penny)