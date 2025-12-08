N = int(input())

result = [0] * 10

def get_page_numbers(num):
    length = len(str(num))
    
    prev_num = 10**(length-1) - 1
    page_numbers(length)

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
                page_numbers(length-i, True)

            prev_num = end

    for s in str(num):
        result[int(s)] += 1

def page_numbers(length, need_zero_pad = False):
    if need_zero_pad:
        result[0] += length - 1

    for i in range(1, length):
        if i == 1:
            for j in range(1, 10):
                result[j] += 1
                if need_zero_pad:
                    result[0] += length - i - 1

        else:
            for j in range(10):
                if j > 0:
                    result[j] += 10 ** (i - 1)

                    if need_zero_pad:
                        result[0] += (10 ** (i - 1)) * (length - i - 1)

                result[j] += 9 * (i - 1) * 10 ** (i - 2)

get_page_numbers(N)

print(*result)