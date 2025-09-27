a, b = map(int, input().split())

matrix = [[0] * (a + 1) for _ in range(a + 1)]

for i in range(b):
    x, y = map(int, input().split())
    matrix[x][y] = 1
    matrix[y][x] = 1

def solve_with_matrix():
    if a % 2 != 0:
        return -1

    n = a // 2
    from itertools import combinations

    for group1 in combinations(range(1, a + 1), n):
        group1 = set(group1)
        group2 = set(range(1, a + 1)) - group1
        
        valid = True

        for u in group1:
            for v in group1:
                if u != v and matrix[u][v] == 1:
                    valid = False
                    break
            if not valid:
                break

        for u in group2:
            for v in group2:
                if u != v and matrix[u][v] == 1:
                    valid = False
                    break
            if not valid:
                break
                
        for u in group1:
            for v in group2:
                if matrix[u][v] == 0:
                    valid = False
                    break
            if not valid:
                break

        if valid:
            return sorted(group1)

    return -1


result = solve_with_matrix()
if result == -1:
    print(-1)
else:
    print(*result)
