import pygame
from figures.point import Point
from figures.polygon import Polygon
from figures.circle import Circle
from figures.rectangle import Rectangle
from figures.square import Square


def convert_color_to_rgb(color, palette):

    if color[0] == "(":
        color = color[1:-1]
        rgb = color.split(",")
        return rgb
    elif color[0] == "#":
        rgb_color = ""
        rgb_color += str(int(color[1:3], 16))
        rgb_color += ","
        rgb_color += str(int(color[3:5], 16))
        rgb_color += ","
        rgb_color += str(int(color[5:7], 16))
        rgb = rgb_color.split(",")

        return rgb
    else:
        return convert_color_to_rgb(palette[color], palette)


class PyGameCanvas:
    def __init__(self, palette, screen, figures):
        self.palette = palette
        self.screen = screen
        self.figures = figures

    def run_pygame(self, generate_png, png_file_name):
        pygame.init()
        display = pygame.display.set_mode((self.screen.get_width(), self.screen.get_height()))

        bg_color = convert_color_to_rgb(self.screen.get_bg_color(), self.palette.get_palette())
        display.fill((int(bg_color[0]), int(bg_color[1]), int(bg_color[2])))

        #pix_arr = pygame.PixelArray(display)

        for figure in self.figures:
            if isinstance(figure, Point):
                #pix_arr[figure.get_x()][figure.get_y()] = (0, 0, 0)
                continue

            elif isinstance(figure, Circle):
                rgb = convert_color_to_rgb(figure.get_color(), self.palette.get_palette())
                pygame.draw.circle(display, (int(rgb[0]), int(rgb[1]), int(rgb[2])),
                                   (figure.get_x(), figure.get_y()), figure.get_radius())

            elif isinstance(figure, Polygon):
                rgb = convert_color_to_rgb(figure.get_color(), self.palette.get_palette())
                pygame.draw.polygon(display, (int(rgb[0]), int(rgb[1]), int(rgb[2])), figure.get_points())

            elif isinstance(figure, Rectangle):
                rgb = convert_color_to_rgb(figure.get_color(), self.palette.get_palette())
                pygame.draw.rect(display, (int(rgb[0]), int(rgb[1]), int(rgb[2])), (
                                                         int(figure.get_x()-(figure.get_width()/2)),
                                                         int(figure.get_y()-(figure.get_height()/2)),
                                                         figure.get_width(),
                                                         figure.get_height()))

            elif isinstance(figure, Square):
                rgb = convert_color_to_rgb(figure.get_color(), self.palette.get_palette())
                pygame.draw.rect(display, (int(rgb[0]), int(rgb[1]), int(rgb[2])), (
                                                         int(figure.get_x()-(figure.get_size()/2)),
                                                         int(figure.get_y()-(figure.get_size()/2)),
                                                         figure.get_size(),
                                                         figure.get_size()))

        if generate_png:
            pygame.image.save(display, png_file_name + ".png")

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            pygame.display.update()
