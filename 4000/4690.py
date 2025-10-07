for a in range(2, 101):
    maximum = a**3
    for b in range(2, 101):
        if b**3 >= maximum: break
        for c in range(b, 101):
            if b**3 + c**3 >= maximum: break
            for d in range(c, 101):
                result = b**3 + c**3 + d**3
                if result > maximum: break

                if result == maximum:
                    print(f"Cube = {a}, Triple = ({b},{c},{d})")