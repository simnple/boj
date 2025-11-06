H1, M1, S1 = map(int, input().split(":"))
H2, M2, S2 = map(int, input().split(":"))
H = M = S = 0

if S2 >= S1:
    S = S2 - S1

else:
    if not M2:
        if not H2:
            H2 = 23
            M2 = 59

        else:
            H2 -= 1
            M2 = 59

    else:
        M2 -= 1
    
    S = 60 + S2 - S1

if M2 >= M1:
    M = M2 - M1

else:
    if not H2:
        H2 = 23

    else:
        H2 -= 1

    M = 60 + M2 - M1

if H2 >= H1:
    H = H2 - H1

else:
    H = 24 + H2 - H1

if H == M == S == 0:
    H = 24
    M = S = 0

print(f"{H:02}:{M:02}:{S:02}")