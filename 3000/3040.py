hat_numbers = [int(input()) for _ in range(9)]
total = sum(hat_numbers)

for i in range(len(hat_numbers)):
    for j in range(i+1, len(hat_numbers)):
        if total - hat_numbers[i] - hat_numbers[j] == 100:
            for k in range(len(hat_numbers)):
                if k != i and k != j:
                    print(hat_numbers[k])
            exit()