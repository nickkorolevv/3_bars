import requests
import json


def get_bars():
    url = "https://devman.org/media/filer_public/\
95/74/957441dc-78df-4c99-83b2-e93dfd13c2fa/bars.json"
    response_from_serv = requests.get(url)
    response_file = response_from_serv.json()
    bars = response_file["features"]
    return bars


def get_max_size():
    buffer_to_findmax = []
    for list_item in get_bars():
        seats = list_item["properties"]["Attributes"]["SeatsCount"]
        buffer_to_findmax.append(seats)
    max_size = max(buffer_to_findmax)
    print("Вместимость самого большого бара {}".format(max_size))
    for list_item in get_bars():
        seats = list_item["properties"]["Attributes"]["SeatsCount"]
        if max_size == seats:
            print("Самый большой бар: ")
            print(list_item["properties"]["Attributes"]["Name"])


def get_min_size():
    buffer_to_findmin = []
    for list_item in get_bars():
        seats = list_item["properties"]["Attributes"]["SeatsCount"]
        buffer_to_findmin.append(seats)
    min_size = min(buffer_to_findmin)
    print("Вместимость самого маленького бара {}".format(min_size))
    for list_item in get_bars():
        seats = list_item["properties"]["Attributes"]["SeatsCount"]
        if min_size == seats:
            print("Самый маленький бар: ")
            print(list_item["properties"]["Attributes"]["Name"])


def find_nearest_bar(x_coord, y_coord):
    coord_buff = []
    for list_item in get_bars():
        coordinates = list_item["geometry"]["coordinates"]
        coord_buff.append(coordinates)
    nearest_bar_buff = []
    for list_item in coord_buff:
        diff_x = x_coord-list_item[0]
        diff_y = y_coord-list_item[1]
        sum_of_diffs = abs(diff_x) + abs(diff_y)
        nearest_bar_buff.append(sum_of_diffs)
        min_coord = min(nearest_bar_buff)
    min_index = nearest_bar_buff.index(min_coord)

    return get_bars()[min_index]["properties"]["Attributes"]["Name"]


def get_input_x():
    x_coord = input("Введите координату х \n")
    try:
        float(x_coord)
    except ValueError:
        print("""Неверный формат координат, координаты должны быть
заданы числом с плавающей точкой""")
    return x_coord


def get_input_y():
    y_coord = input("Введите координату х \n")
    try:
        float(y_coord)
    except ValueError:
        print("""Неверный формат координат, координаты должны быть
заданы числом с плавающей точкой""")
    return y_coord


def bars_print():
    get_min_size()
    get_max_size()
    print("Ближайший к Вам бар: ",
          find_nearest_bar(float(get_input_x()), float(get_input_x())))


def main():
    bars_print()


if __name__ == '__main__':
    main()
