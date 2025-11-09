def turn(current, direction):
    if direction == 1:
        if current == "N":
            return "E"
        elif current == "E":
            return "S"
        elif current == "S":
            return "W"
        else:
            return "N"
    elif direction == 2:
        if current == "N":
            return "S"
        elif current == "E":
            return "W"
        elif current == "S":
            return "N"
        else:
            return "E"
    else:
        if current == "N":
            return "W"
        elif current == "E":
            return "N"
        elif current == "S":
            return "E"
        else:
            return "S"

C = "N"

for _ in range(10):
    C = turn(C, int(input()))

print(C)