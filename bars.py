import requests
import json
from token import token
url = "https://apidata.mos.ru/v1/features/1796"


def get_bars():
    payload={"api_key":token}
    response_from_url = requests.get(url, params=payload)
    r_json = response_from_url.json()
    bars = r_json["features"]
    return bars


def get_min_max():

    # создание списка для поиска max и min
    arr_0 = []
    for list_item in get_bars():
        seats = list_item["properties"]["Attributes"]["SeatsCount"]

# добавляем в список
        arr_0.append(seats)
    max_size = max(arr_0)
    min_size = min(arr_0)
    print("Вместимость самого большого бара {}".format(max_size))
    print("Вместимость самого маленького бара {}".format(min_size))
    for list_item in get_bars():
        seats = list_item["properties"]["Attributes"]["SeatsCount"]
        if max_size == seats:
            print("Самый большой бар: ")
            print(list_item["properties"]["Attributes"]["Name"])
        elif min_size == seats:
            print("Самый маленький бар: ")
            print(list_item["properties"]["Attributes"]["Name"])


def find_bar(x_coord, y_coord):
    arr_1 = []
    for list_item in get_bars():
        coordinates = list_item["geometry"]["coordinates"]
        arr_1.append(coordinates)
    arr_2 = []
    for list_item in arr_1:

        diff_x = x_coord-list_item[0]

# находим разницу по координатам

        diff_y = y_coord-list_item[1]

# находим сумму разности x и y
        sum_of_diffs = abs(diff_x) + abs(diff_y)

        arr_2.append(sum_of_diffs)

# находим минимальное отклонение от координат
        min_coord = min(arr_2)

# находим индекс
    min_index = arr_2.index(min_coord)

    return get_bars()[min_index]["properties"]["Attributes"]["Name"]


def main():
    get_min_max()
    x_coord = input("Введите координату х \n")
    y_coord = input("Введите координату y \n")
    try:
        float(x_coord)
        float(y_coord)
    except ValueError:
        print("Неверный формат координат")
        main()
    print("Ближайший к Вам бар: ", find_bar(float(x_coord), float(y_coord)))


if __name__ == '__main__':
    main()
