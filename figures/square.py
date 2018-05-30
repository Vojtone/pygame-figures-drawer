class Square:
    def __init__(self, json_square_data):
        try:
            self.color = json_square_data["color"]
            self.x = json_square_data["x"]
            self.y = json_square_data["y"]
            self.size = json_square_data["size"]
        except Exception:
            raise Exception("Nie podano wszystkich wymaganych własności dla kwadratu. Figura nie zostanie narysowana.")

    def get_color(self):
        return self.color

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_size(self):
        return self.size
