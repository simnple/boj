while True:
    A, B = map(int, input().split())
    if A == B == 0: break

    C = [2*A-B, 2*B-A]
    if (A + B) % 2 == 0: C.append((A+B)/2)

    print(min(C))