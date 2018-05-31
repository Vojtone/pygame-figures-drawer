class Point:
    def __init__(self, json_point_data):
        try:
            self.x = int(json_point_data["x"])
            self.y = int(json_point_data["y"])
        except Exception:
            raise Exception("Nie podano wszystkich wymaganych własności dla punktu. Figura nie zostanie narysowana.")

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
