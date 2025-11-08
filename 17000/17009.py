A = 0
for i in range(3):
    A += int(input()) * (3 - i)

B = 0
for i in range(3):
    B += int(input()) * (3 - i)

if A > B:
    print("A")
elif A < B:
    print("B")
else:
    print("T")