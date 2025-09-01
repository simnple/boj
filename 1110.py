_ = input()

if len(_) == 1: A, B = int(_), 0
else: A, B = map(int, list(_))

original_num = A * 10 + B
temp_num = -1
count = 0

while original_num != temp_num:
    count += 1

    temp = int(str(A + B)[-1])
    A = B
    B = temp

    temp_num = A * 10 + B

print(count)