import sys

def input(): return sys.stdin.readline().rstrip()

N = int(input())
algo = dict()
for _ in range(N):
    string = input().split()
    if algo.get(int(string[1])) == None:
        algo[int(string[1])] = [string[0]]
    else:
        algo[int(string[1])].append(string[0])

M = int(input())
member = dict()
for _ in range(M):
    string = input().split()
    member[string[0]] = int(string[1])

Q = int(input())
last_member = ""
for _ in range(Q):
    message = input().split()
    if " ".join(message[1:]) == "- chan!":
        last_member = message[0]
        print("hai!")
    
    else:
        level = member[last_member]
        levels = sorted(set([i for i in algo] + [level]))
        
        start = 0
        end = len(levels) - 1
        while start <= end:
            mid = (start + end) // 2

            if levels[mid] > level:
                end = mid - 1
            
            elif levels[mid] < level:
                start = mid + 1
            
            else:
                break

        algos = []

        if algo.get(levels[mid]) == None:
            if mid == 0:
                if len(algo[levels[mid + 1]]) > 1:
                    algos = sorted(algo[levels[mid+1]], reverse=True)[-2:]
                else:
                    algos = [sorted(algo[levels[mid+2]], reverse=True)[-1], algo[levels[mid+1]][0]]
            elif mid == len(levels) - 1:
                if len(algo[levels[mid - 1]]) > 1:
                    algos = sorted(algo[levels[mid-1]], reverse=True)[-2:]
                else:
                    algos = [sorted(algo[levels[mid-2]], reverse=True)[-1], algo[levels[mid-1]][0]]

            else:
                if abs(level - levels[mid-1]) < abs(level - levels[mid+1]):
                    if len(algo[levels[mid-1]]) > 1:
                        algos = sorted(algo[levels[mid-1]], reverse=True)[-2:]
                    elif mid >= 2:
                        if abs(level - levels[mid-2]) < abs(level - levels[mid+1]):
                            algos = [sorted(algo[levels[mid-2]], reverse=True)[-1], algo[levels[mid-1]][0]]
                        elif abs(level - levels[mid-2]) > abs(level - levels[mid+1]):
                            algos = [sorted(algo[levels[mid+1]], reverse=True)[-1], algo[levels[mid-1]][0]]
                        else:
                            algos = [sorted(algo[levels[mid-2]] + algo[levels[mid+1]], reverse=True)[-1], algo[levels[mid-1]][0]]
                    else:
                        algos = [sorted(algo[levels[mid+1]], reverse=True)[-1], algo[levels[mid-1]][0]]

                elif abs(level - levels[mid-1]) > abs(level - levels[mid+1]):
                    if len(algo[levels[mid+1]]) > 1:
                        algos = sorted(algo[levels[mid+1]], reverse=True)[-2:]
                    elif mid <= len(levels) - 3:
                        if abs(level - levels[mid+2]) < abs(level - levels[mid-1]):
                            algos = [sorted(algo[levels[mid+2]], reverse=True)[-1], algo[levels[mid+1]][0]]
                        elif abs(level - levels[mid+2]) > abs(level - levels[mid-1]):
                            algos = [sorted(algo[levels[mid-1]], reverse=True)[-1], algo[levels[mid+1]][0]]
                        else:
                            algos = [sorted(algo[levels[mid-1]] + algo[levels[mid+2]], reverse=True)[-1], algo[levels[mid+1]][0]]
                    else:
                        algos = [sorted(algo[levels[mid-1]], reverse=True)[-1], algo[levels[mid+1]][0]]

                else:
                    algos = sorted(algo[levels[mid+1]] + algo[levels[mid-1]], reverse=True)[-2:]
        else:
            if len(algo[levels[mid]]) > 1:
                algos = sorted(algo[levels[mid]], reverse=True)[-2:]

            else:
                if mid == 0:
                    algos = [sorted(algo[levels[mid+1]], reverse=True)[-1], algo[levels[mid]][0]]
                elif mid == len(levels) - 1:
                    algos = [sorted(algo[levels[mid-1]], reverse=True)[-1], algo[levels[mid]][0]]
                else:
                    if abs(level - levels[mid-1]) < abs(level - levels[mid+1]):
                        algos = [sorted(algo[levels[mid-1]], reverse=True)[-1], algo[levels[mid]][0]]
                    elif abs(level - levels[mid-1]) > abs(level - levels[mid+1]):
                        algos = [sorted(algo[levels[mid+1]], reverse=True)[-1], algo[levels[mid]][0]]
                    else:
                        algos = [sorted(algo[levels[mid+1]] + algo[levels[mid-1]], reverse=True)[-1], algo[levels[mid]][0]]

        print(f"{algos[0]} yori mo {algos[1]}")