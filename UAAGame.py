import random

import pygame
import os
import math

from SpriteSheet import SpriteSheet, scale_image
from World import World, Tile

# game window
SCREEN_WIDTH = 1924
SCREEN_HEIGHT = 1000
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (-1920,32)

pygame.init()


toddler = pygame.image.load("screaming_toddler.jpg")
pygame.display.set_icon(toddler)


Scale = 2.5
BlockXSize = 32
BlockYSize = 64


# Screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
# Title
pygame.display.set_caption('UAA Game')


TileSheet = SpriteSheet("2by1.png")
Selector = TileSheet.get_image(0, 0, BlockXSize, BlockYSize).convert_alpha()
Selector = scale_image(Scale, Selector)

Walls = []
for i in range(5):
    Walls.append(TileSheet.get_image_scale(BlockXSize + BlockXSize * i, 0, BlockXSize, BlockYSize, Scale).convert_alpha())
Floors = []
for i in range(0,4):
    Floors.append(TileSheet.get_image_scale(BlockXSize * i, BlockYSize, BlockXSize, BlockYSize, Scale).convert_alpha())
Props = []
for i in range(10):
    Props.append(TileSheet.get_image_scale(BlockXSize * i, BlockYSize * 2, BlockXSize, BlockYSize, Scale).convert_alpha())

ID_LIST = {
    0: pygame.Surface((0,0)),
    1: Walls[0], # Green Wall
    2: Walls[1], # Bluish Purple Wall
    3: Walls[2], # Yellow/Orange Wall
    4: Walls[3], # Red Wall
    5: Walls[4], # Office Wall

    6: Floors[0], # Grey Floor
    7: Floors[1], # Dark Grey Floor
    8: Floors[2], # Wood Floor
    9: Floors[3], # Checkered Floor

    10: Props[0], # Turkey Run Poster
    11: Props[1], # Dress Poster
    12: Props[2], # Blue Text Poster
    13: Props[3], # Person Poster
    14: Props[4], # Left Arrow Poster
    15: Props[5], # Right Arrow Poster
    16: Props[6], # FRC Poster
    17: Props[7], # Question Poster
    18: Props[8], # Exclamation Poster
    19: Props[9], # Wide Halloween Poster
}

world = World()
world.initChunk(0,0)
world.initChunk(1,0)

BlockXOffset = BlockXSize * Scale / 2
BlockYOffset = BlockXSize * Scale / 2

def draw(XScreenOffset, YScreenOffset):
    global screen, BlockXSize, BlockYSize, Walls, Floors, Props, BlockXOffset, BlockYOffset
    for y in range(world.ChunkYSize):
        xYOffset = BlockYOffset * y + XScreenOffset
        yYOffset = BlockYOffset / 2 * y + YScreenOffset
        for x in range(world.ChunkXSize):
            screen.blit(ID_LIST[world.getTile(x, y).land], (x * BlockXOffset - xYOffset, x * BlockXOffset / 2 + yYOffset))
            screen.blit(ID_LIST[world.getTile(x, y).prop],        (x * BlockXOffset - xYOffset, x * BlockXOffset / 2 + yYOffset))








# Font
gameFont = pygame.font.SysFont('consolas',30)
# Draws Text on screen at x, y
def draw_text(text, _x, _y, color=(255, 255, 255), font=gameFont):
    img = font.render(text, True, color)
    screen.blit(img, (_x, _y))

run = True
clock = pygame.time.Clock()

# Keyboard
movingLeft = False
movingRight = False
movingUp = False
movingDown = False

XScreenOffset = 0
YScreenOffset = 0
cameraSpeed = 128.0

indexFPS = 0
maxFPSIndex = 20
averageFPS = [0] * maxFPSIndex
while run:
    # Clock Speed
    clock.tick()
    FPS = clock.get_fps()

    # Mouse Position
    pos = pygame.mouse.get_pos()
    #print(XScreenOffset, YScreenOffset)
    # Keypresses
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                movingRight = True
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                movingLeft = True
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                movingUp = True
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                movingDown = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                movingRight = False
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                movingLeft = False
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                movingUp = False
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                movingDown = False

    # Screen Movement
    if(movingLeft):
        XScreenOffset -= cameraSpeed / FPS
    if(movingRight):
        XScreenOffset += cameraSpeed / FPS
    if(movingUp):
        YScreenOffset += cameraSpeed / FPS
    if(movingDown):
        YScreenOffset -= cameraSpeed / FPS

    # Background
    screen.fill((17, 16, 27))
    # Draw Tiles
    draw(XScreenOffset, YScreenOffset)

    # Average FPS
    averageFPS.pop(0)
    averageFPS.append(FPS)
    draw_text(str(int(sum(averageFPS) / maxFPSIndex)), 0,0)
    # Puts everything on the display
    pygame.display.update()

pygame.quit()
