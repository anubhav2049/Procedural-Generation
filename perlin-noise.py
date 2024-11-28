from noise import pnoise2
import pygame
import sys


def generate_perlin_noise(width, height, scale=10, octaves=1, persistence=0.5, lacunarity=2.0):
    noise_map = []
    for y in range(height):
        row = []
        for x in range(width):
            value = pnoise2(x/scale, y/scale, octaves=octaves, persistence=persistence, lacunarity= lacunarity)
            row.append(value)

        noise_map.append(row)
    return noise_map

def normalize_noise(noise_map):
    min_val = min(min(row) for row in noise_map)
    max_val = max(max(row) for row in noise_map)

    return [[(value - min_val)/(max_val - min_val) for value in row] for row in noise_map]

def visualize_perlin_noise(noise_map, tile_size=15):
    width = len(noise_map[0])
    height = len(noise_map)

    pygame.init()
    screen = pygame.display.set_mode((width * tile_size, height * tile_size))
    pygame.display.set_caption("Perlin Noise Visualizer")

    for y, row in enumerate(noise_map):
        for x, value in enumerate(row):
            color = int(value*255)
            pygame.draw.rect(screen, (color, color, color), (x*tile_size, y*tile_size, tile_size, tile_size))

    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == "__main__":
    map_width = 100
    map_height = 100
    scale = 20
    octaves = 4
    persistent = 0.5
    lacunarity = 2.0

    noise_map = generate_perlin_noise(map_width, map_height, scale, octaves, persistent, lacunarity)
    normalized_noise_map = normalize_noise(noise_map)
    
    visualize_perlin_noise(normalized_noise_map, tile_size=5)