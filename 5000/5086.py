while True:
    a, b = map(int, input().split())
    if a == b == 0: break

    is_factor = b % a == 0
    is_multiple = a % b == 0
    is_neither = not (is_factor or is_multiple)

    if is_neither:
        print("neither")
    elif is_factor:
        print("factor")
    elif is_multiple:
        print("multiple")