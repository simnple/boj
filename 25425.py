N, M, a, K = map(int, input().split())

other_members = a - K
minimum = other_members + 1 if other_members < N else N
maximum = other_members // M + bool(other_members % M) + 1

print(minimum, maximum)