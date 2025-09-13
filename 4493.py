import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    player1_score = 0
    player2_score = 0

    for __ in range(n):
        player1, player2 = input().split()

        if player1 == player2:
            player1_score += 1
            player2_score += 1

        elif player1 == "R":
            if player2 == "S":
                player1_score += 1

            else:
                player2_score += 1

        elif player1 == "S":
            if player2 == "P":
                player1_score += 1

            else:
                player2_score += 1

        elif player1 == "P":
            if player2 == "R":
                player1_score += 1

            else:
                player2_score += 1
    
    if player1_score > player2_score:
        print("Player 1")

    elif player1_score < player2_score:
        print("Player 2")

    else:
        print("TIE")
