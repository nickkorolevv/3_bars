import json


def get_json():
    with open("bars.json", "r", encoding="utf-8") as file_handler:
        return json.load(file_handler)


def get_bars():
    bars = get_json()["features"]
    return bars


def get_max_size():
    buffer_to_findmax = []
    for list_item in get_bars():
        seats = list_item["properties"]["Attributes"]["SeatsCount"]
        buffer_to_findmax.append(seats)
    max_size = max(buffer_to_findmax)
    return max_size


def get_min_size():
    buffer_to_findmin = []
    for list_item in get_bars():
        seats = list_item["properties"]["Attributes"]["SeatsCount"]
        buffer_to_findmin.append(seats)
    min_size = min(buffer_to_findmin)
    return min_size


def max_bar_name():
    for list_item in get_bars():
        seats = list_item["properties"]["Attributes"]["SeatsCount"]
        if get_max_size() == seats:
            return list_item["properties"]["Attributes"]["Name"]


def min_bar_name():
    for list_item in get_bars():
        seats = list_item["properties"]["Attributes"]["SeatsCount"]
        if get_min_size() == seats:
            return list_item["properties"]["Attributes"]["Name"]


def find_nearest_bar(x_coord, y_coord):
    coord_buff = []
    for list_item in get_bars():
        coordinates = list_item["geometry"]["coordinates"]
        coord_buff.append(coordinates)
    nearest_bar_buff = []
    for list_item in coord_buff:
        diff_x = (x_coord-list_item[0])**2
        diff_y = (y_coord-list_item[1])**2
        sum_of_diffs = diff_x + diff_y
        nearest_bar_buff.append(sum_of_diffs)
        min_coord = min(nearest_bar_buff)
    min_index = nearest_bar_buff.index(min_coord)
    return get_bars()[min_index]["properties"]["Attributes"]["Name"]


def get_input():
    x_coord = input("Введите координату X: \n")
    y_coord = input("Введите координату Y: \n")
    try:
        float(x_coord)
        float(y_coord)
    except ValueError:
        print("""Неверный формат координат, координаты должны быть
    заданы числом с плавающей точкой""")
    return x_coord, y_coord


def printer():
    print("Вместимость самого большого бара: ", get_max_size())
    print("Вместимость самого маленького бара: ", get_min_size())
    print("Самый большой бар: ", max_bar_name())
    print("Самый маленький бар: ", min_bar_name())
    x_coord, y_coord = get_input()
    print("Ближайший к Вам бар: ")
    print(find_nearest_bar(float(x_coord), float(y_coord)))


def main():
    printer()


if __name__ == "__main__":
    main()
