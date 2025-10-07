N = int(input())

cards = list(range(1, N+1))

a = False
while len(cards) > 1:
    if not a:
        if len(cards) % 2: a = not a
        cards = [cards[i] for i in range(1, len(cards), 2)]

    else:
        if len(cards) % 2: a = not a
        cards = [cards[i] for i in range(0, len(cards), 2)]

print(cards[0])