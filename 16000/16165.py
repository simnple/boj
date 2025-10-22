import sys

def input(): return sys.stdin.readline().rstrip()

N, M = map(int, input().split())

teams = dict()
for _ in range(N):
    name = input()
    teams[name] = []
    size = int(input())
    for __ in range(size):
        teams[name].append(input())

for _ in range(M):
    string = input()
    quiz = int(input())

    if quiz == 0:
        for name in sorted(teams[string]):
            print(name)
    
    else:
        for team in teams.keys():
            if string in teams[team]:
                print(team)
                break