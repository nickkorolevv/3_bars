import json
import sys


def load_data(filepath):
    with open(filepath, "r", encoding="utf-8") as file_handler:
        return json.load(file_handler)


def get_bars(bars_info):
    bars = bars_info["features"]
    return bars


def get_max_bar(bars):
    max_bar = max(bars, key=lambda bar: bar["properties"]["Attributes"]["SeatsCount"])
    return max_bar


def get_min_bar(bars):
    min_bar = min(bars, key=lambda bar: bar["properties"]["Attributes"]["SeatsCount"])
    return min_bar


def find_nearest_bar(x_coord, y_coord):
    nearest_bar = min(bars, key=lambda z: ((z["geometry"]["coordinates"][0]-x_coord)**2
                                 +(z["geometry"]["coordinates"][1]-y_coord)**2)**0.5)
    return nearest_bar["properties"]["Attributes"]["Name"]


def get_coords():
    x_coord = input("Введите координату X: \n")
    y_coord = input("Введите координату Y: \n")
    try:
        return float(x_coord), float(y_coord)
    except ValueError:
        print("Неверный формат координат, координаты должны быть "
              "заданы числом с плавающей точкой")


def bar_types(bar_type):
    if bar_type == "max_bar":
        return max_bar
    elif bar_type == "min_bar":
        return min_bar


def print_bar(bar_type, nearest_bar):
    print("Ближайший к Вам бар: ", nearest_bar)
    if bar_type == "max_bar":
        print("Самый большой бар: ", max_bar)
    elif bar_type == "min_bar":
        print("Самый маленький бар: ", min_bar)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    else:
        exit("Не выбран файл")
    bars_info = load_data(filepath)
    bars = get_bars(bars_info)
    min_bar = get_min_bar(bars)
    max_bar = get_max_bar(bars)
    x_coord, y_coord = get_coords()
    if not (x_coord and y_coord):
        exit("Координаты не введены")
    nearest_bar = find_nearest_bar(x_coord, y_coord)
    print_bar("max_bar", nearest_bar)
    print_bar("min_bar", nearest_bar)
