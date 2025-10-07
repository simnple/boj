for i in range(int(input())):
    A, B = input().split()

    num = ""
    for i in range(max(len(A), len(B))):
        multiple = 1
        if len(A) >= i + 1:
            multiple *= int(A[-(i + 1)])
        if len(B) >= i + 1:
            multiple *= int(B[-(i + 1)])
        num = str(multiple) + num
    
    print(int(int(num) == int(A)*int(B)))