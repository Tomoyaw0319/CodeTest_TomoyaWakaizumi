from collections import defaultdict

Q = []

while True:
    line = input().strip()
    if not line:
        break
    a, b, d = map(str.strip, line.split(','))
    Q.append((int(a), int(b), float(d)))


adj = defaultdict(list)
nodes = set()
for a, b, d in Q:
    adj[a].append((b, d))
    nodes.add(a)
    nodes.add(b)

print("ノード一覧:", nodes)
print("隣接リスト:")
for node, edges in adj.items():
    print(f"{node} , {edges}")