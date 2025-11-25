N = int(input())

words = [input() for _ in range(N)]
words_increasing = sorted(words)
words_decreasing = words_increasing[::-1]

if words == words_increasing:
    print("INCREASING")
elif words == words_decreasing:
    print("DECREASING")
else:
    print("NEITHER")