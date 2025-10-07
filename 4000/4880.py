while True:
    a1, a2, a3 = map(int, input().split())
    if a1 == a2 == a3 == 0: break

    if a1 - a2 == a2 - a3:
        print("AP", a3 + a2 - a1)
    
    else:
        print("GP", a3 * (a2 // a1))