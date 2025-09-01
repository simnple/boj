import sys

_ = [list(sys.stdin.readline().replace("\n", "")) for i in range(int(sys.stdin.readline()))]

for text in _:
    while len(text) > 0:
        if text[0] == "(":
            is_find = False
            for i in range(1, len(text)):
                if text[i] == ")":
                    is_find = True
                    del(text[i])
                    del(text[0])
                    break
            
            if is_find == False:
                break
        
        else:
            break

    if len(text) == 0:
        print("YES")
    else:
        print("NO")