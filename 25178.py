def is_valid(first, second):
    first_clean = []
    for s in first:
        if s not in ["a", "e", "i", "o", "u"]:
            first_clean.append(s)

    second_clean = []
    for s in second:
        if s not in ["a", "e", "i", "o", "u"]:
            second_clean.append(s)

    return sorted(first) == sorted(second) and first[0] == second[0] and first[-1] == second[-1] and first_clean == second_clean

N = int(input())
durumari = input()
duramuri = input()

print("YES" if is_valid(durumari, duramuri) else "NO")