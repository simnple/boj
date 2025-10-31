import sys

input = sys.stdin.readline

i = 1
while True:
    a, operator, b = input().rstrip().split()
    a, b = map(int, [a, b])

    if operator == "E": break

    result = "false"
    if operator == ">" and a > b:
        result = "true"

    elif operator == ">=" and a >= b:
        result = "true"

    elif operator == "<" and a < b:
        result = "true"

    elif operator == "<=" and a <= b:
        result = "true"

    elif operator == "==" and a == b:
        result = "true"

    elif operator == "!=" and a != b:
        result = "true"

    print(f"Case {i}: {result}")
    i += 1