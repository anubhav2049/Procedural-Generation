import random
import pygame
import sys


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

def visualize_map(map_data):
    tile_size = 50
    colors = {"grass": (34,139,34), "water": (0,0,255), "mountain": (139, 69, 19)}
    pygame.init()
    screen = pygame.display.set_mode((len(map_data[0])*tile_size, len(map_data)*tile_size))
    pygame.display.set_caption("Map Visualization")

    for y, row in enumerate(map_data):
        for x, tile in enumerate(row):
            color = colors.get(tile, (0, 0, 0))
            pygame.draw.rect(screen, color, (x*tile_size, y*tile_size, tile_size, tile_size))

    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

visualize_map(map_data)
