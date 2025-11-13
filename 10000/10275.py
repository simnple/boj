t = int(input())

for _ in range(t):
    n, a, b = map(int, input().split())
    a_bag = b_bag = 0
    
    day = 0
    stack = [2**n]
    while stack:
        half_n = stack.pop() >> 1

        if half_n <= a - a_bag:
            a_bag += half_n
        else:
            stack.append(half_n)

        if half_n <= b - b_bag:
            b_bag += half_n
        else:
            stack.append(half_n)

        day += 1

    print(day)