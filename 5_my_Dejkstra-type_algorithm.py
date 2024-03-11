nodes = {
    'A': ['B', 'C'],
    'B': ['F', 'C'],
    'C': ['F', 'E'],
    'E': ['J', 'L'],
    'F': ['J'],
    'J': ['L'],
    'L': ['']
         }

distances_between_nodes = {
    'A': 0, 'AB': 2, 'AC': 4, 'BF': 1, 'BC': 1, 'CF': 2,
    'CE': 2, 'EJ': 1, 'EL': 4, 'FJ': 4, 'JL': 1, 'L': 0
    }


start_node = list(nodes)[0]
finish_node = list(nodes)[-1]

parents = {}
min_distance = {}


def dist(parent, child):
    if parent == start_node:
        return distances_between_nodes[parent + child]
    else:
        previous_node = parents[parent]
        k = parent + child
        return distances_between_nodes[k] + dist(previous_node, parent)


for current_node, neighbours in nodes.items():
    if neighbours == ['']:
        break
    for value in neighbours:
        # если в parents нет такого ключа, то добавляем ключ-значение (потомок: родитель)
        if value not in parents:
            parents[value] = current_node
        # рассчитаем дистанцию до текущего узла от начальной точки
        distance = dist(current_node, value)
        # если в min_distance нет такого ключа, то добавляем ключ-значение (узел: расстояние до него)
        if value not in min_distance:
            min_distance[value] = distance
        # если расстояние до текущего узла меньше, чем занесено в словарь min_distance, то меняем значения родителя и
        # дистанции до текущего узла
        if distance < min_distance[value]:
            parents[value] = current_node
            min_distance[value] = distance


def best_way(point):
    if parents[point] == start_node:
        return point + parents[point]
    else:
        return point + best_way(parents[point])


way = best_way(finish_node)[::-1]
way = '-'.join(s for s in way)


print(min_distance[finish_node])
print(way)
