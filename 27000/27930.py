S = input()
korea = []
yonsei = []

for i in range(len(S)):
    if (not korea and S[i] == "K") \
    or (len(korea) == 1 and S[i] == "O") \
    or (len(korea) == 2 and S[i] == "R") \
    or (len(korea) == 3 and S[i] == "E") \
    or (len(korea) == 4 and S[i] == "A"):
        korea.append(S[i])

    if (not yonsei and S[i] == "Y") \
    or (len(yonsei) == 1 and S[i] == "O") \
    or (len(yonsei) == 2 and S[i] == "N") \
    or (len(yonsei) == 3 and S[i] == "S") \
    or (len(yonsei) == 4 and S[i] == "E") \
    or (len(yonsei) == 5 and S[i] == "I"):
        yonsei.append(S[i])

    if len(korea) == 5:
        print("KOREA")
        break
    elif len(yonsei) == 6:
        print("YONSEI")
        break