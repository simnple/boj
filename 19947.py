# A | 1년마다 5% 이율
# B | 3년마다 20% 이율
# C | 5년마다 35% 이율

# N년 채워야 돈이 벌어진다.
# 투자 방식은 매년 바꿀 수 있다.

def get_result(money, max_year, year):
    if max_year == year: return money

    result = []
    if year + 1 <= max_year:
        result.append(get_result(int(money * 1.05), max_year, year + 1))

    if year + 3 <= max_year:
        result.append(get_result(int(money * 1.2), max_year, year + 3))

    if year + 5 <= max_year:
        result.append(get_result(int(money * 1.35), max_year, year + 5))

    return max(result)

H, Y = map(int, input().split())
print(get_result(H, Y, 0))