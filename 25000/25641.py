N = int(input())
STST = input()

while STST.count("s") != STST.count("t"):
    STST = STST[1:]

print(STST)