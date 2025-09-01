# 왼쪽 위 t라 두자.

# N == 1
# 사분면 크기: 1
# 제 1사분면 시작: t
# 제 2사분면 시작: t + 1
# 제 3사분면 시작: t + 2
# 제 4사분면 시작: t + 3

# N 홀수
# 절반 idx: 4 ** (N//2)
# 사분면 크기: 2**(4 * (N // 2))
# 제 1사분면 시작: t
# 제 2사분면 시작: t + 2**(4 * (N // 2))
# 제 3사분면 시작: t + 2**(4 * (N // 2)) * 2
# 제 4사분면 시작: t + 2**(4 * (N // 2)) * 3

# N 짝수
# 절반 idx: 2**(N-1)
# 사분면 크기: 2 + 4*(N//2 - 1)
# 제 1사분면 시작: t
# 제 2사분면 시작: t + 2**(2 + 4*(N//2 - 1))
# 제 3사분면 시작: t + 2**(2 + 4*(N//2 - 1)) * 2
# 제 4사분면 시작: t + 2**(2 + 4*(N//2 - 1)) * 3

def z(n, start, pos):
    x, y = pos
    if n == 1:
        # print(n, start, pos)

        if x < 1 and y < 1:
            return start
        elif x > 0 and y < 1:
            return start+1
        elif x < 1 and y > 0:
            return start+2
        elif x > 0 and y > 0:
            return start+3

    elif n % 2 == 0:
        scale = 2**(2 + 4*(n//2 - 1))
        half_idx = 2**(n-1)

    else:
        scale = 2**(4 * (n // 2))
        half_idx = 4 ** (n//2)

    # print(n, start, pos, scale, half_idx)

    if x < half_idx and y < half_idx:
        # print("1번")
        pos = (x, y)
    elif x > half_idx - 1 and y < half_idx:
        # print("2번")
        start += scale * 1
        pos = (x - half_idx, y)
    elif x < half_idx and y > half_idx - 1:
        # print("3번")
        start += scale * 2
        pos = (x, y - half_idx)
    elif x > half_idx - 1 and y > half_idx - 1:
        # print("4번")
        start += scale * 3
        pos = (x - half_idx, y - half_idx)

    return z(n-1, start, pos)

N, r, c = map(int, input().split())
print(z(N, 0, (c, r)))