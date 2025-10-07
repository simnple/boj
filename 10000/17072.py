char_table = ["#", "o", "+", "-", "."]

def intensity(RGB):
    return 2126 * RGB[0] + 7152 * RGB[1] + 722 * RGB[2]

N, M = map(int, input().split())

for _ in range(N):
    d = list(map(int, input().split()))
    for i in range(0, M*3, 3):
        n = intensity(d[i:i+3]) // 510_000
        print(char_table[n if n < 5 else 4], end="")
    print("")