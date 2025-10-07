while True:
    _ = input().split(" ")
    if _ == ["0", "0"]:
        break
    print(sum(map(int,_)))