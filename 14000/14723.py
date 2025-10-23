N = int(input())

line = 1
while N > line:
    N -= line
    line += 1

a, b = line - N + 1, N
print(a, b)