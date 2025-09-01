name = input().replace(" (", "|").replace(")", "|").split("|")
if len(name) == 1:
    print(name[0], "-", sep="\n")
else:
    print(name[0], name[1], sep="\n")