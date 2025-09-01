ISBN = input()

m = 0
broken_idx = -1
result = 0

for i in range(len(ISBN)):
    if ISBN[i] == "*":
        broken_idx = i
        continue

    if (i + 1) % 2 == 0:
        m += 3 * int(ISBN[i])
    
    else:
        m += int(ISBN[i])

if (broken_idx + 1) % 2 == 0:
    if m % 10 != 0:
        for i in range(1, 10):
            if (m + i*3) % 10 == 0:
                result = i
                break

else:
    result = (10 - (m % 10)) % 10

print(result)