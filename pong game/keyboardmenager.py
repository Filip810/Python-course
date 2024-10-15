class KeyboardManager:
    def __init__(self, screen):
        self.keys_pressed = {
            "w": False,
            "s": False,
            "Up": False,
            "Down": False
        }

        screen.onkeypress(self.press_w, "w")
        screen.onkeyrelease(self.release_w, "w")
        screen.onkeypress(self.press_s, "s")
        screen.onkeyrelease(self.release_s, "s")
        screen.onkeypress(self.press_up, "Up")
        screen.onkeyrelease(self.release_up, "Up")
        screen.onkeypress(self.press_down, "Down")
        screen.onkeyrelease(self.release_down, "Down")

    def press_w(self):
        self.keys_pressed["w"] = True

    def release_w(self):
        self.keys_pressed["w"] = False

    def press_s(self):
        self.keys_pressed["s"] = True

    def release_s(self):
        self.keys_pressed["s"] = False

    def press_up(self):
        self.keys_pressed["Up"] = True

    def release_up(self):
        self.keys_pressed["Up"] = False

    def press_down(self):
        self.keys_pressed["Down"] = True

    def release_down(self):
        self.keys_pressed["Down"] = False

    def is_key_pressed(self, key):
        return self.keys_pressed.get(key, False)