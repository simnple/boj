for _ in range(3):
    result = sum(map(int, input().split()))

    if result == 4: print("E")
    elif result == 3: print("A")
    elif result == 2: print("B")
    elif result == 1: print("C")
    else: print("D")