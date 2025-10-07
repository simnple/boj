___ = 1

while True:
    _ = [list(input()) for __ in range(2)]

    if ("".join(_[0]) == "END") & ("".join(_[1]) == "END"):
        break

    _[0].sort()
    _[1].sort()

    ____ = "same" if _[0] == _[1] else "different"
    print(f"Case {___}: " + ____)

    ___ += 1