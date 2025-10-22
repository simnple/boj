# https://www.acmicpc.net/board/view/149753

_ = list(map(int, input().split(" ")))

if _.count(9):
    print("F")
else:
    print("S")