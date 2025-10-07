_ = int(input())

for i in range(_ - 1, -1, -1):
    print(" " * (_ - i - 1), end="")
    print("*" * (1 + i * 2))