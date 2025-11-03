D = input()
if len(D) == 4:
    print(20)

elif len(D) == 3:
    if int(D[:2]) == 10:
        print(10 + int(D[2]))
    else:
        print(10 + int(D[0]))

else:
    print(int(D[0]) + int(D[1]))