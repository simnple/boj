_ = int(input())

for i in range(_):
    print(" " * (_ - i - 1), end="")
    print("*" * (1 + i * 2))