# _ = [input() for __ in range(2)]

# __ = int(_[0].split(" ")[1])

# print(" ".join(list(map(str, [____ for ____ in list(map(int, _[1].split(" "))) if __ > ____]))))

N, X = map(int, input().split())

A = input().split()

print(" ".join([i for i in A if int(i) < X]))
