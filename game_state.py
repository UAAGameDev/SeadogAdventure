from pygame import K_w, K_a, K_s, K_d # import wasd controls
from pygame import K_UP, K_DOWN, K_RIGHT, K_LEFT

class Universe:
    """
    class that should contain all of the players, characters, and should probably own the camera position too?
    not sure how to structure this as of yet

    """
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

    def __init__(self):
        pass


    def process_keyboard_events(self, keyboard_event, camera: CameraState, player):
        """
        takes a pygame keyboard event, a camera, and a player, and tells them what to do
        """
        # mapping from keys to camera events for now, can add more later
        camera_key_mapping = {
            K_w: lambda: camera.toggle_up(),
            K_UP: lambda: camera.toggle_up(),

            K_a: lambda: camera.toggle_left(),
            K_LEFT: lambda: camera.toggle_left(),

            K_s: lambda: camera.toggle_down(),
            K_DOWN: lambda: camera.toggle_down(),

            K_d: lambda: camera.toggle_right(),
            K_RIGHT: lambda: camera.toggle_right(),
        }

        if keyboard_event in camera_key_mapping:
            # check to see that the keyboard event is in the map, then call what you get back from
            # the dictionary as a function
            camera_key_mapping[keyboard_event]()



