S = input()

last_number = int(S[0])
last_count = 1
total_count = 0

for i in range(1, len(S)):
    if last_number + 1 == int(S[i]):
        last_count += 1

        if last_count == 3 and i == len(S) - 1:
            total_count += 1
    else:
        if last_count == 3:
            total_count += 1

        last_count = 1

    last_number = int(S[i])

print(total_count)