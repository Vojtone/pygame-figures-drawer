import json


class JsonParser:
    def __init__(self, json_file_name):

        try:
            with open(json_file_name) as json_data:
                json_data = json.load(json_data)

            self.figures = json_data["Figures"]
            self.palette = json_data["Palette"]
            self.screen = json_data["Screen"]

        except IOError:
            raise IOError("Coś poszło nie tak podczas otwierania podanego pliku. Sprawdź czy podana nazwa jest prawidłowa.")

    def get_figures(self):
        return self.figures

    def get_palette(self):
        return self.palette

    def get_screen(self):
        return self.screen
