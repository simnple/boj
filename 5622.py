num = [2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 9, 9, 9, 9]
time = 0
for word in input():
    time += num[ord(word) - ord("A")] + 1
print(time)