
num_pads = {
    # char: (num, delay)
    " ": (1, 1),
    "A": (2, 1),
    "B": (2, 2),
    "C": (2, 3),
    "D": (3, 1),
    "E": (3, 2),
    "F": (3, 3),
    "G": (4, 1),
    "H": (4, 2),
    "I": (4, 3),
    "J": (5, 1),
    "K": (5, 2),
    "L": (5, 3),
    "M": (6, 1),
    "N": (6, 2),
    "O": (6, 3),
    "P": (7, 1),
    "Q": (7, 2),
    "R": (7, 3),
    "S": (7, 4),
    "T": (8, 1),
    "U": (8, 2),
    "V": (8, 3),
    "W": (9, 1),
    "X": (9, 2),
    "Y": (9, 3),
    "Z": (9, 4),
}

p, w = map(int, input().split())

total = 0
last_num = -1

for s in input():
    num = num_pads[s][0]
    delay = num_pads[s][1]

    if last_num == num and num > 1:
        total += w

    total += delay * p
    last_num = num

print(total)