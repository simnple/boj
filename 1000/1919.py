from collections import Counter

S_1 = input()
S_2 = input()

print(len(S_1) + len(S_2) - sum((Counter(S_1) & Counter(S_2)).values()) * 2)