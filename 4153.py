while True:
    _ = list(map(int, input().split(" ")))
    
    if _ == [0, 0, 0]:
        break

    _.sort()
    
    if _[2]**2 == _[1]**2 + _[0]**2:
        print("right")
    
    else:
        print("wrong")
