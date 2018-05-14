import requests
import json

url = "https://devman.org/media/filer_public/95/74/\
957441dc-78df-4c99-83b2-e93dfd13c2fa/bars.json"
response = requests.get(url)
bars = response.json()
# поиск по ключу features
dict_bars = bars["features"]
# создание списка для поиска max и min
arr_0 = []

for i in dict_bars:
    seats = i["properties"]["Attributes"]["SeatsCount"]
# добавляем в список
    arr_0.append(seats)

max_size = max(arr_0)
min_size = min(arr_0)
for i in dict_bars:
    seats = i["properties"]["Attributes"]["SeatsCount"]
    if max_size == seats:
        print("Самый большой бар: ")
        print(i["properties"]["Attributes"]["Name"])
    elif min_size == seats:
        print("Самый маленький бар: ")
        print(i["properties"]["Attributes"]["Name"])

print("Вместимость самого большого бара {}".format(max_size))
print("Вместимость самого маленького бара {}".format(min_size))

# поиск по координатам
x_coord = float(input("Введите координаты \n"))
y_coord = float(input("Введите координаты \n"))

arr_1 = []
for i in dict_bars:
    coordinates = i["geometry"]["coordinates"]
    arr_1.append(coordinates)
arr_2 = []
for i in arr_1:

    diff_x = x_coord-i[0]

# находим разницу по координатам

    diff_y = y_coord-i[1]

# находим сумму разности x и y
    sum_of_diffs = abs(diff_x) + abs(diff_y)

    arr_2.append(sum_of_diffs)

# находим минимальное отклонение от координат
    min_coord = min(arr_2)

# находим индекс
min_index = arr_2.index(min_coord)

print("Ближайший к вам бар: ",
      bars["features"][min_index]["properties"]["Attributes"]["Name"])
