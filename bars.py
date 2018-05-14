import requests
import json
url="https://devman.org/media/filer_public/95/74/957441dc-78df-4c99-83b2-e93dfd13c2fa/bars.json"
req=requests.get(url)
bars=req.json()
d=bars["features"] #поиск по ключу features
a=[] #создание списка для поиска max и min
for i in d:
    seats=i["properties"]["Attributes"]["SeatsCount"] #перебираем количество мест
    a.append(seats) #добавляем в список
max_size=max(a) 
min_size=min(a)
for i in d:
    seats=i["properties"]["Attributes"]["SeatsCount"] #перебираем количество мест
    if max_size==seats:
        print("Самый большой бар: ")
        print(i["properties"]["Attributes"]["Name"])
    elif min_size==seats:
        print("Самый маленький бар: ")
        print(i["properties"]["Attributes"]["Name"])

print("Вместимость самого большого бара {}".format(max_size))
print("Вместимость самого маленького бара {}".format(min_size))
#поиск по координатам
x=float(input("Введите координаты\n")) #вводим координаты x
y=float(input("Введите координаты\n")) #вводим координаты y
arr_1=[] 
for i in d:
    coordinates=i["geometry"]["coordinates"]
    arr_1.append(coordinates)
arr_2=[]
for i in arr_1:
    diff_x=x-i[0] # находим разницу по координатам х
    diff_y=y-i[1] # находим разницу по координатам y
    sum_of_diffs=abs(diff_x)+abs(diff_y) # находим сумму разности x и y
    arr_2.append(sum_of_diffs)
    min_coord=min(arr_2) # находим минимальное отклонение от координат
min_index=arr_2.index(min_coord) #находим индекс 
print("Ближайший к вам бар: ",bars["features"][min_index]["properties"]["Attributes"]["Name"])
