def base_converter(n, base):
    chars = [chr(i) for i in range(48, 58)]

    result = []
    while n > 0:
        result.append(chars[n%base])
        n //= base
    return "".join(result[::-1])

n, k = map(int, input().split())
total = 0
for i in base_converter(n, k).split("0"):
    if i: total += int(i)
print(base_converter(total, k))