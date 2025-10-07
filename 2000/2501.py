def get_divisors(x):
    divisors = []
    for i in range(1, int(x**(1/2))+1):
        if x % i == 0:
            divisors.append(i)

            if i * i != x:
                divisors.append(x // i)
    return sorted(divisors)

N, K = map(int, input().split())
divisors = get_divisors(N)

if K <= len(divisors):
    print(get_divisors(N)[K-1])
else:
    print(0)