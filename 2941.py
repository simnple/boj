changed = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
word = input()
for c in changed:
    word = word.replace(c, "1")
print(len(word))