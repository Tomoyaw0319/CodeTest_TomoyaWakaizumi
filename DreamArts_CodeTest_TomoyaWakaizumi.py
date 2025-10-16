Q = []

while True:
    line = input().strip()
    if not line:
        break
    a, b, d = map(str.strip, line.split(','))
    Q.append((int(a), int(b), float(d)))

for f in Q:
    print(f)
