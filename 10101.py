_ = [int(input()) for i in range(3)]

if sum(_) == 180:
    if len(set(_)) == 1:
        print("Equilateral")

    elif len(set(_)) == 2:
        print("Isosceles")
    
    else:
        print("Scalene")

else:
    print("Error")