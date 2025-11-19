def base_converter(n, base):
    chars = [str(i) for i in range(10)] + [chr(i) for i in range(65, 91)]

    result = []
    while n > 0:
        result.append(chars[n%base])
        n //= base
    return "".join(result[::-1])

N, B = map(int, input().split())
print(base_converter(N, B))