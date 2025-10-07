"""
M개의 메달을 K명의 아이들에게 똑같이 나누어 줄 수 있으면 'Yes'를, 아니면 'No'를 출력한다.

두 수 M, K를 입력받는다. 
"""

_ = list(map(int, input().split(" ")))
print("Yes" if _[0] % _[1] == 0 else "No")