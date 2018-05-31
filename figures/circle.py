class Circle:
    def __init__(self, json_circle_data):
        try:
            self.color = json_circle_data["color"]
            self.x = int(json_circle_data["x"])
            self.y = int(json_circle_data["y"])
            self.radius = int(json_circle_data["radius"])
        except Exception:
            raise Exception("Nie podano wszystkich wymaganych własności dla koła. Figura nie zostanie narysowana.")

    def get_color(self):
        return self.color

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_radius(self):
        return self.radius
