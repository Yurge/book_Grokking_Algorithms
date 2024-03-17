import itertools

cities = ['Пушкин', 'Луга', 'Тихвин']
dist_between_cities = {
    'Пушкин-Луга': 130,
    'Луга-Пушкин': 128,
    'Пушкин-Тихвин': 228,
    'Тихвин-Пушкин': 230,
    'Луга-Тихвин': 320,
    'Тихвин-Луга': 320
}


all_routes = itertools.permutations(cities)

best_distance = float('inf')
best_route = ()
for route in all_routes:
    distance = 0
    for index in range(0, len(route) - 1):
        city_to_city = f'{route[index]}-{route[index + 1]}'
        distance += dist_between_cities[city_to_city]
    if distance < best_distance:
        best_distance = distance
        best_route = route

print(f'{best_distance} km')
print('-'.join(best_route))
