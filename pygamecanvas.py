import pygame
from figures.point import Point
from figures.polygon import Polygon
from figures.circle import Circle
from figures.rectangle import Rectangle
from figures.square import Square


def convert_string_rgb_to_int_rgb_list(rgb_color):
    int_rgb_list = []
    rgb_string_list = rgb_color.split(",")
    for color in rgb_string_list:
        if (int(color) < 0) or (int(color) > 255):
            print("Podano nieprawidłowy kolor. Użyty zostanie kolor domyślny - czarny")
            return [0, 0, 0]

        int_rgb_list.append(int(color))
    return int_rgb_list


def convert_color_to_rgb_list(color, palette):

    if color[0] == "(":
        color = color[1:-1]
        return convert_string_rgb_to_int_rgb_list(color)

    elif color[0] == "#":
        if len(color) == 7:
            try:
                rgb_color = ""
                rgb_color += str(int(color[1:3], 16))
                rgb_color += ","
                rgb_color += str(int(color[3:5], 16))
                rgb_color += ","
                rgb_color += str(int(color[5:7], 16))
                return convert_string_rgb_to_int_rgb_list(rgb_color)
            except Exception:
                print("W kolorze w formacie hex podano niedopuszczalny znak. Użyty zostanie kolor domyślny - czarny")
                return convert_string_rgb_to_int_rgb_list("0,0,0")

        elif len(color) == 4:
            full_hex_color = "#" + color[1] + color[1] + color[2] + color[2] + color[3] + color[3]
            return convert_color_to_rgb_list(full_hex_color, palette)
        else:
            print("Podano nieprawidłowy kolor w formacie hex. Użyty zostanie kolor domyślny - czarny")
            return convert_string_rgb_to_int_rgb_list("0,0,0")

    else:
        try:
            return convert_color_to_rgb_list(palette[color], palette)
        except Exception:
            print("Brak koloru '" + color + "' w palecie. Użyty zostanie kolor domyślny - czarny")
            return convert_color_to_rgb_list("(0,0,0)", palette)


def draw_figures(self, display):
    palette = self.palette.get_palette()
    for figure in self.figures:
        if not isinstance(figure, Point):
            rgb = convert_color_to_rgb_list(figure.get_color(), palette)
        if isinstance(figure, Point):
            pygame.draw.rect(display, (0, 0, 0), (figure.get_x(), figure.get_y(), 1, 1))
            # (0, 0, 0) - default black color for Points drawing

        elif isinstance(figure, Circle):
            pygame.draw.circle(display, (rgb[0], rgb[1], rgb[2]),
                               (figure.get_x(), figure.get_y()), figure.get_radius())

        elif isinstance(figure, Polygon):
            pygame.draw.polygon(display, (rgb[0], rgb[1], rgb[2]), figure.get_points())

        elif isinstance(figure, Rectangle):
            pygame.draw.rect(display, (rgb[0], rgb[1], rgb[2]), (
                int(figure.get_x() - (figure.get_width() / 2)),
                int(figure.get_y() - (figure.get_height() / 2)),
                figure.get_width(),
                figure.get_height()))

        elif isinstance(figure, Square):
            pygame.draw.rect(display, (rgb[0], rgb[1], rgb[2]), (
                int(figure.get_x() - (figure.get_size() / 2)),
                int(figure.get_y() - (figure.get_size() / 2)),
                figure.get_size(),
                figure.get_size()))


class PyGameCanvas:
    def __init__(self, palette, screen, figures):
        self.palette = palette
        self.screen = screen
        self.figures = figures

    def run_pygame(self, generate_png, png_file_name):
        pygame.init()

        display = pygame.display.set_mode((self.screen.get_width(), self.screen.get_height()))
        bg_color = convert_color_to_rgb_list(self.screen.get_bg_color(), self.palette.get_palette())
        display.fill((bg_color[0], bg_color[1], bg_color[2]))

        draw_figures(self, display)

        if generate_png:
            pygame.image.save(display, png_file_name + ".png")

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            pygame.display.update()
