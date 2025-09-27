a,b = map(int, input().split())

d = {}
mas = set()
for i in range(b):
    x, y = map(int, input().split())
    mas.add(x)
    if x in d:
        d[x].append(y)
    else:
        d[x] = [y]
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
