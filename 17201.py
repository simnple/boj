N = int(input())
A = input()

last_char = A[0:2]
result = "Yes"
for i in range(0, len(A), 2):
    if A[i:i+2] != last_char:
        result = "No"
        break
    last_char = A[i:i+2]

print(result)