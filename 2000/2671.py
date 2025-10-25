# re 안쓰고 깡구현

import sys

sound = input()

idx = 0
need_zero = True
while idx < len(sound):
    if idx + 2 < len(sound) and sound[idx] == "1" and sound[idx + 1] == "0" and sound[idx + 2] == "0":
        idx += 3
        if idx >= len(sound):
            print("NOISE")
            sys.exit(0)
        while sound[idx] == "0":
            if idx == len(sound) - 1:
                print("NOISE")
                sys.exit(0)
            idx += 1

        while sound[idx] == "1":
            if idx == len(sound) - 1:
                print("SUBMARINE")
                sys.exit(0)
            idx += 1
        
        if not (idx + 1 < len(sound) and sound[idx] == "0" and sound[idx + 1] == "1"):
            if sound[idx - 2] == "1":
                idx -= 1

    elif idx + 1 < len(sound) and sound[idx] == "0" and sound[idx + 1] == "1":
        idx += 2

    else:
        print("NOISE")
        break
else:
    print("SUBMARINE")