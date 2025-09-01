_ = int(input())

for i in range(0, _):
    print(" " * (_ - i - 1), end="")
    print("*" * (i * 2 + 1))

for i in range(_ - 2, -1, -1):
    print(" " * (_ - i - 1), end="")
    print("*" * (i * 2 + 1))
