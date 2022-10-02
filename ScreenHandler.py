"""
Basic code to initialize pygame, I'm a little worried about the potential for circular imports being an issue,
but we'll cross that bridge when we come to it.
"""

import pygame
from pygame.locals import RESIZABLE, FULLSCREEN
from os import environ

class ScreenHandler:

    def __init__(self,
                 game_title="Uaa Game",
                 two_monitors=False):

        # initialize game window
        pygame.init()

        self.screen_width = int(pygame.display.Info().current_w / 1.5)
        self.screen_height = int(pygame.display.Info().current_h / 1.5)
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_width), RESIZABLE)
        self.fullscreen = False

        # These store the width and height for switching between full screen and windowed.
        self.setScreenWidth = self.screen_width
        self.setScreenHeight = self.screen_height

        '''
        DO NOT REMOVE 
        Setting the mode twice ensures the VIDEORESIZE event is called when resizing the screen for the first time.
        Without this the window will not resize properly when the user changes its size for the first time.
        '''
        pygame.display.set_mode((0, 0), FULLSCREEN | RESIZABLE)
        pygame.display.set_mode((self.screen_width, self.screen_height), RESIZABLE)

        if two_monitors:  # Set this to true if you want it to appear on a second monitor
            environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (-self.screen_width, 32)

        # Title
        pygame.display.set_caption(game_title)

        # Icon
        self.icon = pygame.image.load("game_icon.png")
        pygame.display.set_icon(self.icon)

        # running variable
        self.running = True

    def shutdown(self):
        self.running = False

    def toggle_full_screen(self):
        self.fullscreen = not self.fullscreen
        if self.fullscreen:
            # Save windowed window size
            self.setScreenWidth = self.screen_width
            self.setScreenHeight = self.screen_height
            self.screen = pygame.display.set_mode((0, 0), FULLSCREEN | RESIZABLE)
        else:
            self.screen = pygame.display.set_mode(
                (self.setScreenWidth, self.setScreenHeight), RESIZABLE)