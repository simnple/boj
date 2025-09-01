_ = [input() for i in range(3)]

words = ["k", "l", "p"]

for d in _:
    if d[0] in words:
        words.remove(d[0])

print("GLOBAL" if len(words) == 0 else "PONIX")