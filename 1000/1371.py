word_frequency = [0] * 26

while True:
    try:
        S = input()
        for s in S:
            if s == " ": continue
            word_frequency[ord(s) - 97] += 1
    except: break

max_frequency = [0]

for i in range(1, 26):
    if word_frequency[i] > word_frequency[max_frequency[0]]:
        max_frequency = [i]
    elif word_frequency[i] == word_frequency[max_frequency[0]]:
        max_frequency.append(i)

print("".join([chr(i + 97) for i in max_frequency]))