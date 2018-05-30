class Screen:
    def __init__(self, json_screen_data):
        self.width = json_screen_data["width"]
        self.height = json_screen_data["height"]
        self.bg_color = json_screen_data["bg_color"]
        self.fg_color = json_screen_data["fg_color"]

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_bg_color(self):
        return self.bg_color

    def get_fg_color(self):
        return self.fg_color
