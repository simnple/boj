def get_square_amount(n):
    result = 0
    
    for i in range(1, n + 1):
        result += i ** 2
    
    return result

while True:
    N = int(input())
    if N == 0: break

    print(get_square_amount(N))