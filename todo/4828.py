# 평문 조건: 32 ~ 127, < > &은 안됨.

# 평문 인코딩
# &lt; -> <
# &gt; -> >
# &amp; -> &

# &xHEX -> HEX는 0~9, A~F 여야함 (대소문자 가능)
# 양의 짝수 자릿수

import sys

def valid_check(string):
    context = []

    temp = []
    is_open_tag = False
    is_open_and = False

    for s in string:
        if is_open_tag:
            if s == "<": return "invalid"
            elif s == ">":
                is_open_tag = False
                temp.append(s)

                last_slash = -1
                for t in range(len(temp)):
                    if temp[t] == "/":
                        if last_slash == -1:
                            last_slash = t
                        else:
                            return "invalid"
                    elif not (97 <= ord(temp[t]) <= 122 or 48 <= ord(temp[t]) <= 57 or ord(temp[t]) == 47 or ord(temp[t]) == 60 or ord(temp[t]) == 62):
                        return "invalid"

                if temp[1] == "/":
                    if len(temp) < 4: return "invalid"
                else:
                    if len(temp) < 3: return "invalid"
                if temp[-2] != "/":
                    context.append("".join(temp))

                temp = []
            else:
                temp.append(s)

        elif is_open_and:
            if s == "<" or s == ">" or s == "&": return "invalid"

            elif s == ";":
                keyword = "".join(temp)
                if keyword == "&lt" or keyword == "&gt" or keyword == "&amp":
                    is_open_and = False
                    temp = []
                elif temp[1] == "x":
                    is_open_and = False
                    if len(temp) % 2 != 0 or len(temp) == 2: return "invalid"
                    for h in temp[2:]:
                        if not (48 <= ord(h) <= 57 or 97 <= ord(h) <= 102 or 65 <= ord(h) <= 70):
                            return "invalid"
            else:
                temp.append(s)

        else:
            if s == ">": return "invalid"
            elif s == "&":
                is_open_and = True
                temp.append(s)
            elif s == "<":
                is_open_tag = True
                temp.append(s)

        if len(context) > 1:
            if context[-2] == context[-1][0] + context[-1][2:]:
                context.pop()
                context.pop()

    if context or is_open_and or is_open_tag:
        return "invalid"
    else:
        return "valid"

for line in sys.stdin:
    print(valid_check(line.strip()))