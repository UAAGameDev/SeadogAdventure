import pygame
from pygame.locals import VIDEORESIZE, FULLSCREEN, RESIZABLE
from ScreenHandler import ScreenHandler

from SpriteSheet import SpriteSheet, scale_image, draw_text
from game_state import KeyBoardState, CameraState

import World
from NewLevel import newLevel


screen_handler = ScreenHandler()

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


BlockXOffset = BlockXSize * Scale / 2
BlockYOffset = BlockXSize * Scale / 2


def draw(XScreenOffset, YScreenOffset):
    """

    I think we could get away from global variables by building a universe class? then feeding that to a screen
    handler that does this sort of processing?
    """
    global screen_handler, BlockXSize, BlockYSize, Walls, Floors, Props, BlockXOffset, BlockYOffset
    for y in range(World.ChunkYSize):
        xYOffset = BlockYOffset * y + XScreenOffset
        yYOffset = BlockYOffset / 2 * y + YScreenOffset
        for x in range(World.ChunkXSize):
            screen_handler.screen.blit(ID_LIST[newLevel.getTile(x, y).land],
                        (x * BlockXOffset - xYOffset, x * BlockXOffset / 2 + yYOffset))
            screen_handler.screen.blit(ID_LIST[newLevel.getTile(x, y).solidProp],
                        (x * BlockXOffset - xYOffset, x * BlockXOffset / 2 + yYOffset))
            screen_handler.screen.blit(ID_LIST[newLevel.getTile(x, y).prop],
                        (x * BlockXOffset - xYOffset, x * BlockXOffset / 2 + yYOffset))




# Camera
camera_state = CameraState()
# Keyboard
keyboard_state = KeyBoardState(camera_state, screen_handler, None)  # camera state, screen handler, and player go here

# FPS Counter
indexFPS = 0
maxFPSIndex = 20
averageFPS = [0] * maxFPSIndex
while screen_handler.running:
    # Clock Speed
    clock.tick()
    FPS = clock.get_fps()

    # Mouse Position
    pos = pygame.mouse.get_pos()
    # Keypresses
    for event in pygame.event.get():
        # System Events
        if event.type == pygame.QUIT:  # Shut down pygame
            screen_handler.shutdown()

        if event.type == VIDEORESIZE:  # if window is resized change the window
            # Center camera in window so the view appears to have not changed
            camera_state.XScreenOffset += (screen_handler.screen_width - event.w) / 2
            camera_state.YScreenOffset -= (screen_handler.screen_height - event.h) / 2
            screen_handler.screen_width = event.w
            screen_handler.screen_height = event.h
            if not FULLSCREEN:
                screen_handler.screen = pygame.display.set_mode(
                    (screen_handler.screen_width, screen_handler.screen_height), RESIZABLE)

        # Keyboard Events
        if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            # process the events that occur on the key up or the key down
            keyboard_state.process_key_up_or_down(event.key)

        if event.type == pygame.KEYDOWN:
            # process the events that are solely on key down (like window resizing stuff)
            keyboard_state.process_key_down(event.key)



    # Screen Movement
    if camera_state.moving_left:
        camera_state.XScreenOffset -= camera_state.cameraSpeed / FPS
    if camera_state.moving_right:
        camera_state.XScreenOffset += camera_state.cameraSpeed / FPS
    if camera_state.moving_up:
        camera_state.YScreenOffset += camera_state.cameraSpeed / FPS
    if camera_state.moving_down:
        camera_state.YScreenOffset -= camera_state.cameraSpeed / FPS

    # Background
    screen_handler.screen.fill((17, 16, 27))
    # Draw Tiles
    draw(camera_state.XScreenOffset, camera_state.YScreenOffset)

    # Calculate and Draw FPS Counter
    averageFPS.pop(0)
    averageFPS.append(FPS)
    draw_text(screen_handler.screen, gameFont, str(int(sum(averageFPS) / maxFPSIndex)), 0, 0)
    # Puts everything on the display
    pygame.display.update()

pygame.quit()
