class Polygon:
    def __init__(self, json_point_data):
        try:
            self.color = json_point_data["color"]
            self.points = json_point_data["points"]
        except Exception:
            raise Exception("Nie podano wszystkich wymaganych własności dla wielokąta. Figura nie zostanie narysowana.")

    def get_color(self):
        return self.color

    def get_points(self):
        return self.points
