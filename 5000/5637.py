import sys
import re

input = sys.stdin.readline

is_loop = True
longest_word = ""

while is_loop:
    data = input().rstrip()
    if data.endswith("E-N-D"):
        is_loop = False
        data = data[:-5]
    
    for s in re.findall("[a-zA-Z-]+", data):
        if len(s) > len(longest_word):
            longest_word = s

print(longest_word.lower())