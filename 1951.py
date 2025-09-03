# 1의자리 9
# 10의자리 90 * 2
# 100의자리 900 * 3
# 1000의자리 9000 * 4

N = int(input())

total = ((N - 10 ** (len(str(N)) - 1) + 1) * len(str(N))) % 1234567
for i in range(len(str(N)) - 1):
    total += ((10 ** i) * 9 * (i + 1)) % 1234567

print(total % 1234567)