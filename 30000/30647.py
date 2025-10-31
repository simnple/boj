import sys, json

input = sys.stdin.readline

N = int(input())

raw_json = ""
for _ in range(N):
    raw_json += input().rstrip()

data = sorted(json.loads(raw_json), key=lambda x: (-x["score"], x["name"]))

prev_score = data[0]["score"]
rank = 1

for i in range(N):
    if prev_score != data[i]["score"]: rank = i + 1

    if not data[i]["isHidden"]:
        print(f"{rank} {data[i]['name']} {data[i]['score']}")
        
    prev_score = data[i]["score"]