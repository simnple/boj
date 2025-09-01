def get_gcd(num1, num2):
    num = []
    n = 2

    while n <= num1 and n <= num2:
        if num1 % n == 0 and num2 % n == 0:
            num.append(n)
            num1 //= n
            num2 //= n
            continue

        n += 1

    result = 1
    for i in num:
        result *= i

    return result

x, y = map(int, input().split())

gcd = get_gcd(x, y)
print(gcd)
print(x*y//gcd)