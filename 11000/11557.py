T = int(input())

for _ in range(T):
    N = int(input())

    result = ""
    largest_value = 0
    for _ in range(N):
        name, value = input().split()
        value = int(value)

        if int(value) > largest_value:
            result = name
            largest_value = int(value)
    
    print(result)