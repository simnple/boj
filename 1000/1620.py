import sys

def input(): return sys.stdin.readline().rstrip()

N, M = map(int, input().split())

name_dic = {}
num_dic = []

def add_poke(name, num):
    global name_dic, num_dic
    name_dic[name] = num
    num_dic.append(name)

for _ in range(N):
    add_poke(input(), _+1)

for _ in range(M):
    data = input()
    if data.isdigit():
        print(num_dic[int(data)-1])
    else:
        print(name_dic[data])