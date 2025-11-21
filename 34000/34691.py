import sys

input = sys.stdin.readline

while True:
    S = input().rstrip()
    if S == "end": break
    elif S == "animal": print("Panthera tigris")
    elif S == "tree": print("Pinus densiflora")
    elif S == "flower": print("Forsythia koreana")