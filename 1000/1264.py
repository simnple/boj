words = ["a", "e", "i", "o", "u"]

while True:
    _ = input()

    if _ == "#":
        break

    count = 0

    for w in words:
        count += _.lower().count(w)

    print(count)