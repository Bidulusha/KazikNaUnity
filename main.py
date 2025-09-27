a, b = map(int, input().split())

# Создаём матрицу смежности (a x a), изначально заполненную нулями
matrix = [[0] * (a + 1) for _ in range(a + 1)]

# Заполняем матрицу рёбрами
for i in range(b):
    x, y = map(int, input().split())
    matrix[x][y] = 1
    matrix[y][x] = 1  # для неориентированного графа


# Пытаемся разделить на две доли
# Для полного двудольного графа матрица должна иметь блочную структуру:
# [ 0 B ]
# [ B 0 ]

def solve_with_matrix():
    if a % 2 != 0:
        return -1  # нечётное количество вершин - не может быть сбалансированным

    n = a // 2  # размер каждой доли

    # Пробуем разные разбиения вершин на две группы
    from itertools import combinations

    # Перебираем все возможные первые доли размера n
    for group1 in combinations(range(1, a + 1), n):
        group1 = set(group1)
        group2 = set(range(1, a + 1)) - group1

        # Проверяем, что это полный двудольный граф
        valid = True

        # Проверяем рёбра внутри group1 - их не должно быть
        for u in group1:
            for v in group1:
                if u != v and matrix[u][v] == 1:
                    valid = False
                    break
            if not valid:
                break

        # Проверяем рёбра внутри group2 - их не должно быть
        for u in group2:
            for v in group2:
                if u != v and matrix[u][v] == 1:
                    valid = False
                    break
            if not valid:
                break

        # Проверяем рёбра между group1 и group2 - должны быть все
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
