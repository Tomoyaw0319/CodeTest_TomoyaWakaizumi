from collections import defaultdict
import sys

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

if not nodes:
    sys.exit(0)

best_len = -1.0
best_path = []

#最大値摘出
max_out = {u: (max((w for _, w in adj[u]), default=0.0)) for u in nodes}

for u in adj:
    adj[u].sort(key=lambda x: x[1], reverse=True)

sys.setrecursionlimit(1 << 25)

def dfs(start, u, visited, path, cur_len, to_start=True):

    global best_len, best_path

    if cur_len > best_len:
        best_len = cur_len
        best_path = path[:]

    if adj[u]:
        optimistic = cur_len + adj[u][0][1]
        if optimistic <= best_len:
            return
        
    for v, w in adj[u]:
        if v not in visited:
            visited.add(v)
            path.append(v)
            dfs(start, v, visited, path, cur_len + w, to_start=to_start)
            path.pop()
            visited.remove(v)
        elif to_start and v == start and len(path) > 1:
            total = cur_len + w
            if total > best_len:
                best_len = total
                best_path = path[:] + [start]

#test
for s in nodes:
    dfs(s, s, {s}, [s], 0.0, to_start=True)

print("best_len:", best_len)
print("path:", " -> ".join(map(str, best_path)))