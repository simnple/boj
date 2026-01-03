L, U = map(int, input().split())

def get_numbers(num):
    length = len(str(num))

    prev_num = 10**(length-1) - 1
    numbers(length)

    end = 0
    for i in range(length):
        diff = num // 10**(length-1-i) % 10 - (prev_num + 1) // 10**(length-1-i) % 10
        if diff != 0:
            start = prev_num + 1
            end = prev_num + diff * 10**(length-1-i)

            for s in str(start)[:i]:
                result[int(s)] += end - start + 1

            for j in range(start // 10**(length-1-i) % 10, end // 10**(length-1-i) % 10 + 1):
                result[j] += 10**(length-i-1)
                numbers(length-i)

            prev_num = end

    for s in str(num):
        result[int(s)] += 1

def numbers(length):
    for i in range(1, length):
        if i == 1:
            for j in range(1, 10):
                result[j] += 1

        else:
            for j in range(10):
                if j > 0:
                    result[j] += 10 ** (i - 1)

                result[j] += 9 * (i - 1) * 10 ** (i - 2)

L_sum = 0
if L > 0:
    result = [0] * 10
    if L == 1:
        L_sum = 0

    else:
        get_numbers(L - 1)
        L_sum = sum([i * j for i, j in enumerate(result)])

U_sum = 0
if U > 0:
    result = [0] * 10
    get_numbers(U)
    U_sum = sum([i * j for i, j in enumerate(result)])

print(U_sum - L_sum)