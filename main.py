#!/usr/bin/python3

import sys

from jsonparser import JsonParser
from palette import Palette
from screen import Screen
from figures.point import Point
from figures.polygon import Polygon
from figures.rectangle import Rectangle
from figures.square import Square
from figures.circle import Circle
from pygamecanvas import PyGameCanvas


def validate_command_line_args(parsed_args):
    how_many_args = len(parsed_args)

    if (how_many_args != 2) and (how_many_args != 4):
        print("Podano nieprawidłową liczbę argumentów.")
        return False

    elif how_many_args == 4:
        if (parsed_args[2] != "-o") and (parsed_args[2] != "--output"):
            print("Argumenty muszą zostać podane w następującej kolejności:\n "
                  "plik.json -o (lub --output) plik_do_zapisu")
            return False

    return True


def create_figure_obj(figure):
    figure_type = figure["type"]

    if figure_type == "point":
        return Point(figure)
    elif figure_type == "polygon":
        return Polygon(figure)
    elif figure_type == "rectangle":
        return Rectangle(figure)
    elif figure_type == "square":
        return Square(figure)
    elif figure_type == "circle":
        return Circle(figure)
    else:
        raise Exception("Podano nieprawidłowy typ figury. Figura ta nie zostanie narysowana.")


def main():
    args = sys.argv

    if not validate_command_line_args(args):
        return

    json_file_name = args[1]
    if len(args) == 2:
        generate_png = False
        png_file_name = None
    else:
        generate_png = True
        png_file_name = args[3]

    try:
        data_to_draw = JsonParser(json_file_name)
    except IOError as err:
        print(err)
        return

    palette = Palette(data_to_draw.get_palette())
    screen = Screen(data_to_draw.get_screen())
    figures = []

    for figure in data_to_draw.get_figures():
        try:
            figures.append(create_figure_obj(figure))
        except Exception as err:
            print(err)

    canvas = PyGameCanvas(palette, screen, figures)
    canvas.run_pygame(generate_png, png_file_name)

    print("elo")
    return


if __name__ == "__main__":
    main()
