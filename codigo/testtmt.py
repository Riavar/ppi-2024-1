import pygame
import pytmx

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ejemplo de Mapa TMX en Pygame")

# Cargar el archivo TSX
tmx_data = pytmx.util_pygame.load_pygame("./mapa/EcoGuerra.tsx")

# Cargar la imagen del tileset
tileset_image = pygame.image.load("./mapa/ecoguerra.png")

# Escalar el tileset según sea necesario
tile_width, tile_height = tmx_data.tilewidth, tmx_data.tileheight
tileset_image = pygame.transform.scale(tileset_image, (tile_width, tile_height))

# Obtener el número de filas y columnas del mapa
map_width, map_height = tmx_data.width, tmx_data.height

# Crear una matriz para almacenar los IDs de los tiles
map_data = [[-1 for _ in range(map_width)] for _ in range(map_height)]

# Llenar la matriz con los IDs de los tiles del mapa
for layer in tmx_data.visible_layers:
    if isinstance(layer, pytmx.TiledTileLayer):
        for y in range(layer.height):
            for x in range(layer.width):
                tile = layer.content2D[y][x]
                if tile:
                    map_data[y][x] = tile.gid - 1  # gid comienza desde 1, restar 1 para el índice de la imagen del tile

# Función para dibujar el mapa
def draw_map():
    for y in range(map_height):
        for x in range(map_width):
            tile_id = map_data[y][x]
            if tile_id >= 0:
                tile_rect = pygame.Rect(x * tile_width, y * tile_height, tile_width, tile_height)
                screen.blit(tileset_image, tile_rect, tmx_data.get_tile_image_by_gid(tile_id))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))  # Limpiar pantalla
    draw_map()  # Dibujar el mapa en la pantalla

    pygame.display.flip()

pygame.quit()
