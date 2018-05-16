import json
import sys


def get_info(filepath):
    with open(filepath, "r", encoding="utf-8") as file_handler:
        return json.load(file_handler)


def get_bars(bars_info):
    bars = bars_info["features"]
    return bars


def get_max_bar_name(bars):
    max_bar = max(bars, key=lambda bar: bar["properties"]["Attributes"]["SeatsCount"])
    return max_bar["properties"]["Attributes"]["Name"]


def get_max_seats(bars):
    max_seats = max(bars, key=lambda bar: bar["properties"]["Attributes"]["SeatsCount"])
    return max_seats["properties"]["Attributes"]["SeatsCount"]


def get_min_bar_name(bars):
    min_bar = min(bars, key=lambda bar: bar["properties"]["Attributes"]["SeatsCount"])
    return min_bar["properties"]["Attributes"]["Name"]


def get_min_seats(bars):
    min_seats = min(bars, key=lambda bar: bar["properties"]["Attributes"]["SeatsCount"])
    return min_seats["properties"]["Attributes"]["SeatsCount"]


def find_nearest_bar(x_coord, y_coord):
    nearest_bar = min(bars, key=lambda z: ((z["geometry"]["coordinates"][0]-x_coord)**2
                                 +(z["geometry"]["coordinates"][1]-y_coord)**2)**0.5)
    return (nearest_bar["properties"]["Attributes"]["Name"])


def get_coord():
    x_coord = input("Введите координату X: \n")
    y_coord = input("Введите координату Y: \n")
    try:
        float(x_coord)
        float(y_coord)
        return float(x_coord), float(y_coord)
    except ValueError:
        print("Неверный формат координат, координаты должны быть")
        print("заданы числом с плавающей точкой")


def print_bar(max_bar_name, min_bar_name, nearest_bar):
    max_seats = get_max_seats(bars)
    min_seats = get_min_seats(bars)
    print("Вместимость самого большого бара: ", max_seats)
    print("Вместимость самого маленького бара: ", min_seats)
    print("Самый большой бар: ", max_bar_name)
    print("Самый маленький бар: ", min_bar_name)
    print("Ближайший к Вам бар: ")
    print(nearest_bar)



if __name__ == "__main__":
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    bars_info = get_info(filepath)
    bars = get_bars(bars_info)
    min_bar_name = get_min_bar_name(bars)
    max_bar_name = get_max_bar_name(bars)
    x_coord, y_coord = get_coord()
    nearest_bar = find_nearest_bar(x_coord, y_coord)
    print_bar(max_bar_name, min_bar_name, nearest_bar)