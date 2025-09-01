# 소문자 / 대문자 / 숫자 / 공백

while True:
    try:
        lower = upper = number = space = 0

        for _ in input():
            if _.islower():
                lower += 1
            
            elif _.isupper():
                upper += 1

            elif _.isnumeric():
                number += 1
            
            elif _.isspace():
                space += 1

        print(lower, upper, number ,space)

    except: break