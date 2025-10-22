ascii_to_char = {
    46: ".",
    79: "O",
    45: "|",
    124: "-",
    47: "\\",
    92: "/",
    94: "<",
    60: "v",
    118: ">",
    62: "^"
}

N, M = map(int, input().split())
_ = [input() for i in range(N)]

for i in range(M - 1, -1, -1):
    for j in range(N):
        print(ascii_to_char[ord(_[j][i])], end="")
    print()