import sys

input = sys.stdin.readline

hex_words = [i for i in range(48, 58)] + [i for i in range(65, 71)] + [i for i in range(97, 103)]
tag_words = [i for i in range(48, 58)] + [i for i in range(97, 123)]

def check(S):
    context = []

    i = 0
    while i < len(S):
        if i + 3 < len(S) and S[i:i+4] == "&lt;":
            i += 4
        elif i + 3 < len(S) and S[i:i+4] == "&gt;":
            i += 4
        elif i + 4 < len(S) and S[i:i+5] == "&amp;":
            i += 5
        elif i + 1 < len(S) and S[i:i+2] == "&x":
            i += 2
            count = 0
            while i < len(S):
                if ord(S[i]) in hex_words:
                    i += 1
                    count += 1
                elif S[i] == ";":
                    i += 1
                    break
                else:
                    return False
            else:
                return False
            if count % 2 != 0 or count == 0:
                return False
        elif S[i] == "<":
            i += 1
            if i < len(S):
                if S[i] == "/":
                    i += 1
                    tag = []
                    while i < len(S):
                        if ord(S[i]) in tag_words:
                            tag.append(S[i])
                            i += 1
                        elif S[i] == ">":
                            i += 1
                            break
                        else:
                            return False
                    else:
                        return False
                    if not tag:
                        return False
                    elif not context:
                        return False
                    elif context[-1] != "".join(tag):
                        return False
                    else:
                        context.pop()
                else:
                    tag = []
                    do_not_add = False
                    while i < len(S):
                        if ord(S[i]) in tag_words:
                            tag.append(S[i])
                            i += 1
                        elif S[i] == ">":
                            i += 1
                            break
                        elif i + 1 < len(S) and S[i:i+2] == "/>":
                            i += 2
                            do_not_add = True
                            break
                        else:
                            return False
                    else:
                        return False
                    if do_not_add:
                        continue
                    elif not tag:
                        return False
                    else:
                        context.append("".join(tag))
            else:
                return False
        else:
            if S[i] in ["&", ">"]:
                return False
            i += 1
    return not context

for S in sys.stdin:
    print("valid" if check(S.rstrip()) else "invalid")