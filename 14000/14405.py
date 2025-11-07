import sys

input = sys.stdin.readline

S = input().rstrip()

i = 0
while i < len(S):
    if i + 1 < len(S) and S[i] == "p" and S[i + 1] == "i":
        i += 2
    
    elif i + 1 < len(S) and S[i] == "k" and S[i + 1] == "a":
        i += 2
    
    elif i + 2 < len(S) and S[i] == "c" and S[i + 1] == "h" and S[i + 2] == "u":
        i += 3
    
    else:
        break

if i == len(S):
    print("YES")
else:
    print("NO")