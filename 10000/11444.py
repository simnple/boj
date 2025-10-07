n = int(input())

divisor = 1_000_000_007
period = 0

fibo = [0, 1]
for i in range(2, n+1):
    fibo.append((fibo[i-1] % divisor + fibo[i-2] % divisor) % divisor)
    if fibo[-3:] == [0, 1, 1] and i-2 != 0:
        period = i-2
        break

print(fibo[n % period] if period > 0 else fibo[n])