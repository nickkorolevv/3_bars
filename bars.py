import json
import sys
import os


def load_data(filepath):
    with open(filepath, "r", encoding="utf-8") as file_handler:
        try:
            return json.load(file_handler)
        except ValueError:
            return None


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
    nearest_bar = min(
        bars,
        key=lambda z: (
            (z["geometry"]["coordinates"][0]-x_coord)**2 +
            (z["geometry"]["coordinates"][1]-y_coord)**2
        ) ** 0.5
    )
    return nearest_bar


def get_coords():
    x_coord = input("Введите координату X: \n")
    y_coord = input("Введите координату Y: \n")
    try:
        return float(x_coord), float(y_coord)
    except ValueError:
        return None, None


def print_bar(bar_type, bar_name):
    print(bar_type, bar_name["properties"]["Attributes"]["Name"])


if __name__ == "__main__":
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    else:
        exit("Файл не выбран. Выберите файл")
    if not(os.path.exists(filepath)):
        exit("Файла нет в директории")
    bars_info = load_data(filepath)
    if bars_info is None:
        exit("Файл не является JSON объектом")
    bars = get_bars(bars_info)
    min_bar = get_min_bar(bars)
    max_bar = get_max_bar(bars)
    x_coord, y_coord = get_coords()
    if not (x_coord and y_coord):
        exit("Координаты не введены или неверный формат")
    nearest_bar = find_nearest_bar(x_coord, y_coord)
    print_bar("Самый большой бар", max_bar)
    print_bar("Самый маленький бар", min_bar)
    print_bar("Ближайший к Вам бар", nearest_bar)
