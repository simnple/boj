def solution(n, base):
    chars = [chr(i) for i in range(48, 58)] + [chr(i) for i in range(65, 91)]

    result = []
    while n > 0:
        result.append(chars[n%base])
        n //= base
    return "".join(result[::-1])

N, B = map(int, input().split())
print(solution(N, B))