while True:
    data = input()
    if data == "end": break

    ttt = [["", "", ""], ["", "", ""], ["", "", ""]]
    for s in range(len(data)):
        ttt[s // 3][s % 3] = data[s]
    for t in ttt:
        print(t)