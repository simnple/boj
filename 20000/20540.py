mbti_words = ["I", "E", "S", "N", "T", "F", "J", "P"]

for word in input():
    mbti_words.remove(word)

print("".join(mbti_words))