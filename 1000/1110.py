def plus_cycle(n):
    s1, s2 = n // 10, n % 10
    return int(f"{s2}{(s1 + s2) % 10}")

N = int(input())

num = plus_cycle(N)
count = 1

while N != num:
    num = plus_cycle(num)
    count += 1

print(count)