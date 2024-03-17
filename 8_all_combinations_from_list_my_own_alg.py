cities = ['Пушкин', 'Луга', 'Тихвин', 'Всеволожск']

all_routes = [cities]


def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number - 1)


def routes(route):
    ways = []
    for x in range(1, len(route)):
        for y in range(0, len(route) - x):
            points = route.copy()
            ind_1, ind_2 = y, y+x
            points[ind_1], points[ind_2] = points[ind_2], points[ind_1]
            if points not in ways:
                ways.append(points)
    for way in ways:
        if way not in all_routes:
            all_routes.append(way)


max_count = factorial(len(cities))

for one in all_routes:
    if len(all_routes) == max_count:
        break
    else:
        routes(one)

print(max_count)
print(len(all_routes))
# print(all_routes)
