import sys

input = sys.stdin.readline
INF = sys.maxsize

def solution():
    result = None
    result_sum = INF

    for start in range(N - 2):
        mid = start + 1
        end = N - 1

        while mid < end:
            value_sum = A[start] + A[mid] + A[end]
            value_sum_abs = abs(value_sum)
            if result_sum > value_sum_abs:
                result = (A[start], A[mid], A[end])
                result_sum = value_sum_abs

            if value_sum == 0:
                return result

            elif value_sum > 0:
                end -= 1

            else:
                mid += 1

    return result

N = int(input())
A = sorted(list(map(int, input().split())))

print(*solution())