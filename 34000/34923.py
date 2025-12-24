h_1, m_1 = map(int, input().split(":"))
h_2, m_2 = map(int, input().split(":"))

clock_1, clock_2 = sorted([h_1 * 60 + m_1, h_2 * 60 + m_2])

clock_wise = abs(clock_1 - clock_2)
counter_clock_wise = abs(12 * 60 + clock_1 - clock_2)

print(min(clock_wise, counter_clock_wise) * 6)