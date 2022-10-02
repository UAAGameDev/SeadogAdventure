"""
Basic code to initialize pygame, I'm a little worried about the potential for circular imports being an issue,
but we'll cross that bridge when we come to it.
"""

import pygame
from pygame.locals import RESIZABLE, FULLSCREEN
from os import environ

def initialize_screen(two_monitors=False,
                      game_title="Uaa Game") -> tuple[pygame.display, int, int]:
    """
    this function initializes pygame and sets up the main window.

    """

    # initialize game window
    pygame.init()
    SCREEN_WIDTH = int(pygame.display.Info().current_w / 1.5)
    SCREEN_HEIGHT = int(pygame.display.Info().current_h / 1.5)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), RESIZABLE)
    fullscreen = False
    # These store the width and height for switching between full screen and windowed.
    setScreenWidth = SCREEN_WIDTH
    setScreenHeight = SCREEN_HEIGHT
    '''
    DO NOT REMOVE 
    Setting the mode twice ensures the VIDEORESIZE event is called when resizing the screen for the first time.
    Without this the window will not resize properly when the user changes its size for the first time.
    '''
    pygame.display.set_mode((0, 0), FULLSCREEN | RESIZABLE)
    pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), RESIZABLE)

    if two_monitors:  # Set this to true if you want it to appear on a second monitor
        environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (-SCREEN_WIDTH, 32)

    # Title
    pygame.display.set_caption(game_title)

    # after the screen is configured, return a tuple with the screen object, the width and the height
    return screen, SCREEN_WIDTH, SCREEN_HEIGHT

    # Icon
    toddler = pygame.image.load("screaming_toddler.jpg")
    pygame.display.set_icon(toddler)