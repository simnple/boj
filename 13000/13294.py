import math

def get_n(n):
    nums = {"1": 1, "2": 2, "6": 3, "120": 5, "720": 6}
    if nums.get(n): return nums[n]

    log_sum = 0
    i = 1

    while True:
        log_sum += math.log10(i)

        if int(log_sum) + 1 == len(n):
            return i

        i += 1

n_factorial = input()

print(get_n(n_factorial))