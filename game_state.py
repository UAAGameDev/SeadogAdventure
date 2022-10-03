from pygame import K_w, K_a, K_s, K_d, K_F11, K_ESCAPE # import wasd controls
from pygame import K_UP, K_DOWN, K_RIGHT, K_LEFT
from ScreenHandler import ScreenHandler
class Universe:
    """
    class that should contain all of the players, characters, and should probably own the camera position too?
    not sure how to structure this as of yet

    """
    def __init__(self):
        # game objects

        self.sprites = []
        self.players = []
        self.objects = []

        # states
        self.game_state = None
        self.camera_state = None
        self.player_state = None
        self.keyboard_state = None


class GameState:
    def __init__(self):
        pass


class CameraState:

    def __init__(self):
        self.moving_up = False
        self.moving_down = False
        self.moving_left = False
        self.moving_right = False

        self.XScreenOffset = 0
        self.YScreenOffset = 0
        self.cameraSpeed = 128.0

    def toggle_up(self):
        if self.moving_up:
            self.moving_up = False
        else:
            self.moving_up = True

    def toggle_down(self):
        if self.moving_down:
            self.moving_down = False
        else:
            self.moving_down = True

    def toggle_left(self):
        if self.moving_left:
            self.moving_left = False
        else:
            self.moving_left = True

    def toggle_right(self):
        if self.moving_right:
            self.moving_right = False
        else:
            self.moving_right = True


class PlayerState:

    def __init__(self):
        pass




class KeyBoardState:

    def __init__(self, camera: CameraState,
                 screen_handler: ScreenHandler,
                 player: PlayerState):
        self.camera = camera
        self.screen_handler = screen_handler
        self.player = player

        # these events get fired on up or down key input (press or depress)
        self.control_mapping_up_or_down = {
            K_w: lambda: self.camera.toggle_up(),
            K_UP: lambda: self.camera.toggle_up(),

            K_a: lambda: self.camera.toggle_left(),
            K_LEFT: lambda: self.camera.toggle_left(),

            K_s: lambda: self.camera.toggle_down(),
            K_DOWN: lambda: self.camera.toggle_down(),

            K_d: lambda: self.camera.toggle_right(),
            K_RIGHT: lambda: self.camera.toggle_right(),

        }

        # these keyboard events only are triggered when the key is pressed
        self.control_mapping_down_only = {
            K_F11: lambda: self.screen_handler.toggle_full_screen(),
            K_ESCAPE: lambda: self.screen_handler.shutdown()
        }


    def process_key_up_or_down(self, keyboard_event):
        # take the keyboard event, if it's in the control map, execute the appropriate control
        if keyboard_event in self.control_mapping_up_or_down:
            # check to see that the keyboard event is in the map, then call what you get back from
            # the dictionary as a function
            self.control_mapping_up_or_down[keyboard_event]()

    def process_key_down(self, keyboard_event):
        # take the keyboard event, if it's in the control map, execute the appropriate control
        if keyboard_event in self.control_mapping_down_only:
            # check to see that the keyboard event is in the map, then call what you get back from
            # the dictionary as a function
            self.control_mapping_down_only[keyboard_event]()




