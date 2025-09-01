def get_cantor(string):
    if len(string)//3 == 0: return string
    return get_cantor(string[:len(string)//3]) + [" "] * (len(string)//3) + get_cantor(string[-len(string)//3:])

while True:
    try:
        N = int(input())
        print("".join(get_cantor(["-"] * (3 ** N))))
    
    except:
        break