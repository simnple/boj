blacklist = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']

text = input().split()

print("".join([text[0][:1].upper()] + [s[:1].upper() for s in text[1:] if s not in blacklist]))