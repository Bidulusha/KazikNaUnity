a, b = map(int, input().split())

edges = [[] for _ in range(a + 1)]
for i in range(b):
    x, y = map(int, input().split())
    edges[x].append(y)
    edges[y].append(x)

# Преобразуем в множества для удобства
for i in range(1, a + 1):
    edges[i] = set(edges[i])

# Пытаемся раскрасить граф в 2 цвета (проверка на двудольность)
color = [0] * (a + 1)
from collections import deque


def is_bipartite(start):
    q = deque([start])
    color[start] = 1
    part1, part2 = [], []

    while q:
        u = q.popleft()
        if color[u] == 1:
            part1.append(u)
        else:
            part2.append(u)

        for v in edges[u]:
            if color[v] == 0:
                color[v] = 3 - color[u]  # 1->2, 2->1
                q.append(v)
            elif color[v] == color[u]:
                return False, [], []

    return True, part1, part2


# Проверяем двудольность
bipartite, part1, part2 = is_bipartite(1)

# Если не все вершины посещены (граф несвязный)
if len(part1) + len(part2) != a:
    print(-1)
elif not bipartite:
    print(-1)
else:
    # Проверяем сбалансированность
    if len(part1) != len(part2):
        print(-1)
    else:
        # Проверяем полноту связей
        n = len(part1)
        expected_edges = n * n

        if b != expected_edges:
            print(-1)
        else:
            # Проверяем, что все возможные рёбра присутствуют
            part1_set, part2_set = set(part1), set(part2)
            valid = True

            for u in part1:
                if edges[u] != part2_set:
                    valid = False
                    break

            for u in part2:
                if edges[u] != part1_set:
                    valid = False
                    break

            if valid:
                print(*sorted(part1))
            else:
                print(-1)
