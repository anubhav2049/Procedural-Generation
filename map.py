import random


map_width, map_height = 10, 10
map_data = [[0 for _ in range(map_width)] for _ in range(map_height)]

for y in range(map_height):
    for x in range(map_width):
        map_data[y][x] = random.choice(['grass', 'water', 'mountain'])

for row in map_data:
    print(" ".join(row))

def generate_cave(map_width, map_height, fill_chance=0.45, steps=4):
    cave = [[random.random() < fill_chance for _ in range(map_width)] for _ in range(map_height)]

    def count_neighbors(x, y):
        return sum(
            cave[y + dy][x + dx]
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]
            if 0 <= x + dx < map_width and 0 <= y + dy < map_height
        )
    
    for _ in range(steps):
        cave = [[count_neighbors(x,y) >= 5 if cave[y][x] else count_neighbors(x,y) >= 4 for x in range(map_width)] for y in range(map_height)]

    return cave

cave = generate_cave(20, 10)
for row in cave:
    print(" ".join(["#" if cell else "." for cell in row]))