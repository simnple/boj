import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

plus_count = 0
x_count = 0
result = 1 # = 한개는 기본으로

for i in range(N):
    if nums[i] > 0:
        x_count = N - i
        break

# x 개수 + 곱하기 개수
result += x_count
result += x_count - 1

is_first = True
is_zero = True

# x 처리
for i in range(N):
    if nums[i] == 0: is_zero = True; continue
    elif nums[i] == 1:
        # x^3 + x 같은 경우 (연속되지 않은 x)
        if is_zero and not is_first:
            result += 1
        plus_count += 1
        is_first = False
    else:
        result += len(str(nums[i]))
        plus_count += 1
        is_first = False

# 상수 처리
if nums[N]:
    result += len(str(nums[N]))
    plus_count += 1

# 더하기 처리
result += plus_count - 1

print(result)