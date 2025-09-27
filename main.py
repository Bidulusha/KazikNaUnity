a,b = map(int, input().split())

c = b

d = {}
mas = set()
for i in range(c):
    x, y = map(int, input().split())
    if x == y:
        b = 0
    mas.add(x)
    if x in d:
        d[x].append(y)
    else:
        d[x] = [y]

if b != 0:
    c = mas.pop()
    a = d[c]
    for i in d:
        if d[i] != a:
            print(-1)
            break
    else:
        mas.add(c)
        if len(mas) != len(d[c]):
            print(-1)
        else:
            print(*sorted(mas))
else:
    print(-1)
