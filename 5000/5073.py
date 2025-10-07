while True:
    side_length = list(map(int, input().split()))
    if side_length == [0, 0, 0]: break
    
    left_side_length = side_length[:]
    left_side_length.remove(max(side_length))

    result = len(set(side_length)) if max(side_length) < sum(left_side_length) else -1
    
    if result == 1:
        print("Equilateral")
    elif result == 2:
        print("Isosceles")
    elif result == 3:
        print("Scalene")
    else:
        print("Invalid")