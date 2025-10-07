char_dict = {chr(i): 0 for i in list(range(65, 91)) + list(range(97, 123))}
char_dict["A"] = 1
char_dict["a"] = 1
char_dict["B"] = 2
char_dict["b"] = 1
char_dict["D"] = 1
char_dict["d"] = 1
char_dict["e"] = 1
char_dict["g"] = 1
char_dict["O"] = 1
char_dict["o"] = 1
char_dict["P"] = 1
char_dict["p"] = 1
char_dict["Q"] = 1
char_dict["q"] = 1
char_dict["R"] = 1
char_dict["@"] = 1

count = 0
for s in input():
    if s in char_dict:
        count += char_dict[s]
print(count)