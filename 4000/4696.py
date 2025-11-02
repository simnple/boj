while True:
    value = float(input())
    if value == 0: break

    print(f"{1 + value + value ** 2 + value ** 3 + value ** 4:.02f}")