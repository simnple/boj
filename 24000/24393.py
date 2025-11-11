import sys

input = sys.stdin.readline

N = int(input())
cards = [False] * 27
cards[0] = True

for _ in range(N):
    A = list(map(int, input().split()))
    new_cards = []

    left_card_idx = 0
    right_card_idx = 13

    for i in range(len(A)):
        if i % 2 == 1:
            for j in range(left_card_idx, left_card_idx + A[i]):
                new_cards.append(cards[j])

            left_card_idx += A[i]

        else:
            for j in range(right_card_idx, right_card_idx + A[i]):
                new_cards.append(cards[j])

            right_card_idx += A[i]

    cards = new_cards

print(cards.index(True) + 1)