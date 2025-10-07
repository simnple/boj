import sys

def FizzBuzz(num: int) -> str:
    result = ""
    if num % 3 == 0:
        result += "Fizz"
    
    if num % 5 == 0:
        result += "Buzz"
    
    if len(result) == 0:
        result += str(num)

    return result

_ = [sys.stdin.readline().replace("\n", "") for i in range(3)]

if _[0].isnumeric():
    print(FizzBuzz(int(_[0]) + 3))

elif _[1].isnumeric():
    print(FizzBuzz(int(_[1]) + 2))

elif _[2].isnumeric():
    print(FizzBuzz(int(_[2]) + 1))
