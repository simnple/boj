# A분 후 -> 마지막 버스
# B분 후 -> 마지막 열차

# 찬솔이 위치: 버스 정류장
# 지하철 승강장 -> N분

N, A, B = map(int, input().split(" "))
print("Bus" if B > A else "Subway" if B < A else "Anything")