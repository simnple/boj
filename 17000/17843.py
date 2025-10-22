import sys

input = sys.stdin.readline

def calculate_degree(main_degree, other_degree):
    result = []
    result.append(360 - main_degree + other_degree)
    result.append(abs(main_degree - other_degree))

    return min(result)

T = int(input())

for _ in range(T):
    h, m, s = map(int, input().split())

    s_degree = s * 6
    m_degree = (m + (s_degree / 360)) * 6
    h_degree = (h + (m_degree / 360)) * 30

    time_degrees = [s_degree, m_degree, h_degree]
    time_degrees.sort()

    degrees = []
    
    degrees.append(calculate_degree(time_degrees[0], time_degrees[1]))
    degrees.append(calculate_degree(time_degrees[1], time_degrees[2]))
    degrees.append(calculate_degree(time_degrees[2], time_degrees[0]))

    print(min(degrees))