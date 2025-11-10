H1, M1 = map(int, input().split())
H2, M2 = map(int, input().split())
N = int(input())

count = 0

while H1 < H2 or (H1 == H2 and M1 <= M2):
    if H1 // 10 == N:
        count += 1
    elif H1 % 10 == N:
        count += 1
    elif M1 // 10 == N:
        count += 1
    elif M1 % 10 == N:
        count += 1

    M1 += 1
    if M1 == 60:
        M1 = 0
        H1 += 1

print(count)