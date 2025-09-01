N = int(input())

for i in range(N):
    if i == 0 or i == N-1:
        print("*" * N)
        continue

    if i < N/2:
        print("*" + " " * (i - 1) + "*" + " " * (N - 2*(i + 1)) + "*" * (1 if (N - 2*(i + 1)) >= 0 else 0) + " " * (i - 1) + "*")

    else:
        print("*" + " " * (N - i - 2) + "*" + " " * (N - 2*(N - i)) + "*" + " " * (N - i - 2) + "*")