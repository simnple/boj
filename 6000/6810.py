isbn = 91

for i in range(3):
    if i % 2 == 0:
        isbn += int(input())
    else:
        isbn += int(input()) * 3

print(f"The 1-3-sum is {isbn}")