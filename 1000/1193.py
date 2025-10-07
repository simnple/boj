X = int(input())

a = b = 1
is_turn = True
is_up = True

for _ in range(1, X):
    if a == 1 and is_turn:
        b += 1
        is_up = False
        is_turn = False
    elif b == 1 and is_turn:
        a += 1
        is_up = True
        is_turn = False
    elif is_up:
        a -= 1
        b += 1
        if a == 1: is_turn = True
    else:
        a += 1
        b -= 1
        if b == 1: is_turn = True

print(f"{a}/{b}")