X = int(input())

item_count = line_number = line_sum = 0

while item_count + line_number < X:
    item_count += line_number
    line_number += 1

line_sum = line_number + 1

if line_number % 2 == 0:
    a = X - item_count
    b = line_sum - a

else:
    b = X - item_count
    a = line_sum - b

print(f"{a}/{b}")