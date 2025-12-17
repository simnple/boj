import math

def get_m_factorial(m):
    factorial = {1: 1, 2: 1, 3: 1, 5: 3, 6: 3}
    if factorial.get(m): return factorial[m]

    log_sum = 0
    for i in range(1, m + 1):
        log_sum += math.log10(i)
    return int(log_sum) + 1

T = int(input())

for _ in range(T):
    m = int(input())
    print(get_m_factorial(m))
