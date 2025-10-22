def solution():
    N = input()

    H, E, L, O, W, R, D = [-1] * 7
    if 5 <= len(N) <= 6:
        for o in range(10):
            for d in range(10):
                if ((o + d == int(N[-1]) or o + d == int(N[-1]) + 10)) and len(set([o, d])) == 2:
                    for l in range(10):
                        if (((2*l == int(N[-2]) or 2*l == int(N[-2]) + 10) and o + d < 10) or ((2*l == int(N[-2]) - 1 or (2*l == int(N[-2]) + 9 and 2*l >= 10)) and o + d >= 10)) and len(set([o, d, l])) == 3:
                            for r in range(10):
                                if (((l + r == int(N[-3]) or l + r == int(N[-3]) + 10) and 2*l < 10) or ((l + r == int(N[-3]) - 1 or (l + r == int(N[-3]) + 9 and l + r >= 10)) and 2*l >= 10)) and len(set([o, d, l, r])) == 4:
                                    for e in range(10):
                                        if (((e + o == int(N[-4]) or e + o == int(N[-4]) + 10) and l + r < 10) or ((e + o == int(N[-4]) - 1 or (e + o == int(N[-4]) + 9 and e + o >= 10)) and l + r >= 10)) and len(set([o, d, l, r, e])) == 5:
                                            for h in range(1, 10):
                                                for w in range(1, 10):
                                                    if ((h + w == int(N[:-4]) and e + o < 10) or (h + w == int(N[:-4]) - 1 and e + o >= 10)) and len(set([o, d, l, r, e, h, w])) == 7:
                                                        H = h
                                                        E = e
                                                        L = l
                                                        O = o
                                                        W = w
                                                        R = r
                                                        D = d
                                                        break

                                                    else: continue
                                        else: continue
                                else: continue
                        else: continue
                else: continue

    if H == -1:
        print("No Answer")
    else:
        hello = "".join(list(map(str, [H, E, L, L, O])))
        world = "".join(list(map(str, [W, O, R, L, D])))

        print(f"  {hello}")
        print(f"+ {world}")
        print("-------")
        if len(N) == 5:
            print(f"  {N}")
        else:
            print(f" {N}")

solution()