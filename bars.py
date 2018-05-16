import json
import sys


def get_json(filepath):
    with open(filepath, "r", encoding="utf-8") as file_handler:
        return json.load(file_handler)


def get_bars():
    data_file = get_json(filepath)
    bars = data_file["features"]
    return bars


def max_bar_name():
    bars = get_bars()
    max_bar = max(bars, key=lambda bar: bar["properties"]["Attributes"]["SeatsCount"])
    return max_bar["properties"]["Attributes"]["Name"], max_bar["properties"]["Attributes"]["SeatsCount"]


def min_bar_name():
    bars = get_bars()
    min_bar = min(bars, key=lambda bar: bar["properties"]["Attributes"]["SeatsCount"])
    return min_bar["properties"]["Attributes"]["Name"], min_bar["properties"]["Attributes"]["SeatsCount"]


def find_nearest_bar(x_coord, y_coord):
    coord_buff = []
    data_file = get_bars()
    for list_item in data_file:
        coordinates = list_item["geometry"]["coordinates"]
        coord_buff.append(coordinates)
    nearest_bar_buff = []
    for list_item in coord_buff:
        diff_x = (x_coord-list_item[0])**2
        diff_y = (y_coord-list_item[1])**2
        sum_sqr_of_diffs = (diff_x + diff_y)**0.5
        nearest_bar_buff.append(sum_sqr_of_diffs)
        min_coord = min(nearest_bar_buff)
    min_index = nearest_bar_buff.index(min_coord)
    return get_bars()[min_index]["properties"]["Attributes"]["Name"]


def get_coord():
    x_coord = input("Введите координату X: \n")
    y_coord = input("Введите координату Y: \n")
    try:
        float(x_coord)
        float(y_coord)
        return x_coord, y_coord
    except ValueError:
        print("""Неверный формат координат, координаты должны быть
    заданы числом с плавающей точкой""")



def print_bar():
    min_bar, min_size_of_bar = min_bar_name()
    max_bar, max_size_of_bar = max_bar_name()
    print("Вместимость самого большого бара: ", max_size_of_bar)
    print("Вместимость самого маленького бара: ", min_size_of_bar)
    print("Самый большой бар: ", max_bar)
    print("Самый маленький бар: ", min_bar)
    x_coord, y_coord = get_coord()
    print("Ближайший к Вам бар: ")
    print(find_nearest_bar(float(x_coord), float(y_coord)))


def main():
    print_bar()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        filepath = format(sys.argv[1])
    else:
        filepath = input("Укажите путь до json файла: ")
    main()