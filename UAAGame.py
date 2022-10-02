import pygame
from pygame.locals import VIDEORESIZE, FULLSCREEN, RESIZABLE
from screen_setup import initialize_screen

from SpriteSheet import SpriteSheet, scale_image, draw_text
from World import World, Tile

screen, SCREEN_WIDTH, SCREEN_HEIGHT = initialize_screen(two_monitors=False)

# Icon
toddler = pygame.image.load("screaming_toddler.jpg")
pygame.display.set_icon(toddler)
# Game Clock
clock = pygame.time.Clock()
# Font
gameFont = pygame.font.SysFont('consolas', 30)

# Sprites
Scale = 2.5
BlockXSize = 32
BlockYSize = 64

TileSheet = SpriteSheet("2by1.png")
Selector = TileSheet.get_image(0, 0, BlockXSize, BlockYSize).convert_alpha()
Selector = scale_image(Scale, Selector)

Walls = []
for i in range(5):
    Walls.append(
        TileSheet.get_image_scale(BlockXSize + BlockXSize * i, 0, BlockXSize, BlockYSize, Scale).convert_alpha())
Floors = []
for i in range(0, 4):
    Floors.append(TileSheet.get_image_scale(BlockXSize * i, BlockYSize, BlockXSize, BlockYSize, Scale).convert_alpha())
Props = []
for i in range(10):
    Props.append(
        TileSheet.get_image_scale(BlockXSize * i, BlockYSize * 2, BlockXSize, BlockYSize, Scale).convert_alpha())

ID_LIST = {
    0: pygame.Surface((0, 0)),
    1: Walls[0],  # Green Wall
    2: Walls[1],  # Bluish Purple Wall
    3: Walls[2],  # Yellow/Orange Wall
    4: Walls[3],  # Red Wall
    5: Walls[4],  # Office Wall

    6: Floors[0],  # Grey Floor
    7: Floors[1],  # Dark Grey Floor
    8: Floors[2],  # Wood Floor
    9: Floors[3],  # Checkered Floor

    10: Props[0],  # Turkey Run Poster
    11: Props[1],  # Dress Poster
    12: Props[2],  # Blue Text Poster
    13: Props[3],  # Person Poster
    14: Props[4],  # Left Arrow Poster
    15: Props[5],  # Right Arrow Poster
    16: Props[6],  # FRC Poster
    17: Props[7],  # Question Poster
    18: Props[8],  # Exclamation Poster
    19: Props[9],  # Wide Halloween Poster
}

world = World()
world.initChunk(0, 0)
world.initChunk(1, 0)

BlockXOffset = BlockXSize * Scale / 2
BlockYOffset = BlockXSize * Scale / 2


def draw(XScreenOffset, YScreenOffset):
    global screen, BlockXSize, BlockYSize, Walls, Floors, Props, BlockXOffset, BlockYOffset
    for y in range(world.ChunkYSize):
        xYOffset = BlockYOffset * y + XScreenOffset
        yYOffset = BlockYOffset / 2 * y + YScreenOffset
        for x in range(world.ChunkXSize):
            screen.blit(ID_LIST[world.getTile(x, y).land],
                        (x * BlockXOffset - xYOffset, x * BlockXOffset / 2 + yYOffset))
            screen.blit(ID_LIST[world.getTile(x, y).solidProp],
                        (x * BlockXOffset - xYOffset, x * BlockXOffset / 2 + yYOffset))
            screen.blit(ID_LIST[world.getTile(x, y).prop],
                        (x * BlockXOffset - xYOffset, x * BlockXOffset / 2 + yYOffset))


run = True

# Keyboard
movingLeft = False
movingRight = False
movingUp = False
movingDown = False
# Camera
XScreenOffset = 0
YScreenOffset = 0
cameraSpeed = 128.0
# FPS Counter
indexFPS = 0
maxFPSIndex = 20
averageFPS = [0] * maxFPSIndex
while run:
    # Clock Speed
    clock.tick()
    FPS = clock.get_fps()

    # Mouse Position
    pos = pygame.mouse.get_pos()
    # Keypresses
    for event in pygame.event.get():
        # System Events
        if event.type == pygame.QUIT:  # Shut down pygame
            run = False
        if event.type == VIDEORESIZE:  # if window is resized change the window
            # Center camera in window so the view appears to have not changed
            XScreenOffset += (SCREEN_WIDTH - event.w) / 2
            YScreenOffset -= (SCREEN_HEIGHT - event.h) / 2
            SCREEN_WIDTH = event.w
            SCREEN_HEIGHT = event.h
            if (not FULLSCREEN):
                screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), RESIZABLE)

        # Key Events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                movingRight = True
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                movingLeft = True
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                movingUp = True
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                movingDown = True

            if event.key == pygame.K_ESCAPE:  # Quit Game
                run = False
            if event.key == pygame.K_F11:  # Toggles Fullscreen
                fullscreen = not fullscreen
                if (fullscreen):
                    # Save windowed window size
                    setScreenWidth = SCREEN_WIDTH
                    setScreenHeight = SCREEN_HEIGHT
                    screen = pygame.display.set_mode((0, 0), FULLSCREEN | RESIZABLE)
                else:
                    screen = pygame.display.set_mode((setScreenWidth, setScreenHeight), RESIZABLE)

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
    if (movingLeft):
        XScreenOffset -= cameraSpeed / FPS
    if (movingRight):
        XScreenOffset += cameraSpeed / FPS
    if (movingUp):
        YScreenOffset += cameraSpeed / FPS
    if (movingDown):
        YScreenOffset -= cameraSpeed / FPS

    # Background
    screen.fill((17, 16, 27))
    # Draw Tiles
    draw(XScreenOffset, YScreenOffset)

    # Calculate and Draw FPS Counter
    averageFPS.pop(0)
    averageFPS.append(FPS)
    draw_text(screen, gameFont, str(int(sum(averageFPS) / maxFPSIndex)), 0, 0)
    # Puts everything on the display
    pygame.display.update()

pygame.quit()
