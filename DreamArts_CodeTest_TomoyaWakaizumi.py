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


start_order = sorted(nodes, key=lambda x: max_out.get(x, 0.0), reverse=True)

for s in start_order:
    visited = set([s])
    dfs(s, s, visited, [s], 0.0, to_start=True)

if best_len < 0 and nodes:
    best_path = [min(nodes)]

def normalize_cycle(path):
    if len(path) >= 2 and path[0] == path[-1]:
        core = path[:-1]
        min_id = min(core)
        idx = core.index(min_id)
        path = core[idx:] + core[:idx] + [min_id]
    return path

best_path = normalize_cycle(best_path)

out = sys.stdout
for nid in best_path:
    print(nid, file=out)