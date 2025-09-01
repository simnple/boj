___ = []
while True:
    _ = input()
    if _ == "0":
        break
    ___.append(_)

for _ in ___:
    if len(_) == 1:
        print("yes")
        continue

    for __ in range(len(_) // 2):
        if _[__] == _[-1 * __ - 1]:
            if __ == len(_) // 2 - 1:
                print("yes")

        else:
            print("no")
            break