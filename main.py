a, b = map(int, input().split())

d = {}
for i in range(1, a + 1):
    d[i] = set()


for i in range(b):
    x, y = map(int, input().split())
    d[x].add(y)

groups = {}
for vertex, neighbors in d.items():
    key = tuple(sorted(neighbors))
    if key not in groups:
        groups[key] = []
    groups[key].append(vertex)


if len(groups) == 2:
    group1, group2 = groups.values()


    if len(group1) == len(group2):
        expected_edges = len(group1) * len(group2)
        if b == expected_edges:
            print(*sorted(group1))
        else:
            print(-1)
    else:
        print(-1)
else:
    print(-1)
