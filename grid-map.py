import random

map_width, map_height = 10, 10
map_data = [[0 for _ in range(map_width)] for _ in range(map_height)]

for y in range(map_height):
    for x in range(map_width):
        map_data[y][x] = random.choice(['grass', 'water', 'mountain'])

for row in map_data:
    print(" ".join(row))


