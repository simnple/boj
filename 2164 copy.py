from collections import deque

for N in range(1, 20):
    cards = deque(range(1, N + 1))

    while len(cards) > 1:
        cards.popleft()
        card = cards.popleft()
        cards.append(card)

    print(N, cards[0])