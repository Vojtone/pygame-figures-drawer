class Rectangle:
    def __init__(self, json_rectangle_data):
        try:
            self.color = json_rectangle_data["color"]
            self.x = int(json_rectangle_data["x"])
            self.y = int(json_rectangle_data["y"])
            self.width = int(json_rectangle_data["width"])
            self.height = int(json_rectangle_data["height"])
        except Exception:
            raise Exception("Nie podano wszystkich wymaganych własności dla prostokąta. Figura nie zostanie narysowana.")

    def get_color(self):
        return self.color

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height
