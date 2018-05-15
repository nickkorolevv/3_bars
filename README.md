
# Ближайшие бары

[Описание]
На сайте data.mos.ru есть много разных данных, в том числе список московских баров. Его можно скачать в формате JSON. Для этого нужно:
зарегистрироваться на сайте и получить ключ API;
скачать файл по ссылке вида https://apidata.mos.ru/v1/features/1796?api_key={place_your_API_key_here}.

Скачать файл можно по ссылке https://devman.org/media/filer_public/95/74/957441dc-78df-4c99-83b2-e93dfd13c2fa/bars.json

   

Этот скрипт рассчитывает:

 - самый большой бар; 
 - самый маленький бар;
 - самый близкий бар (текущие gps-координаты пользователь введет с клавиатуры).





# Как запустить
Для запуска скрипта Вам понадобятся следующие библиотеки

 - [ ] json
 - [ ] requests
 
 Установить их можно в консоли по команде
 

    pip install requests

 При запуске скрипта он попросит Вас ввести координаты, они должны быть в формате числа с плавающей точкой.

## Пример вывода скрипта

 - [ ] Самый большой бар: 
 - [ ] Спорт бар «Красная машина»
 - [ ] Самый маленький бар: 
 - [ ] Бар в Деловом центре Яуза
 - [ ] Вместимость самого большого бара 450
 - [ ] Вместимость самого маленького бара 0
 - [ ] Введите координаты
 - [ ] 37.923458345334
 - [ ] Введите координаты
 - [ ] 55.46356456456456
 - [ ] Ближайший к вам бар:  Таверна


# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
