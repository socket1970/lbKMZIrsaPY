# Лабораторная работа по предмету КМЗИ. Шифр RSA
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/funny_m4n)
***
## Описание
Алгоритм реализован на Python.

Схема шифра:
```
    1. Alice:           e = m^Db mod Nb;
    2. Alice -> Bob:    e;
    3. Bob:         m = m` = e^Cb mod Nb;    
```

В качестве дополнения к этой лабораторной работе можно посмотреть [декодирование из числового формата в символьный.](https://github.com/socket1970/KMZIcryptogramLB) Однако, оно уже встроено в ***эту*** реализацию алгоритма RSA.
***
### Задание.
Заданы параметры шифра:
* сообщение;
* p - простое число;
* q - простое число;
* С - секретный ключ;

Производится расчет недостающих ключей и переписки. Переписка выводится на экран.
***
### Компиляция.
Запустить файл ***main.py***, предварительно изменив в нем значения на свои.
***

## !!! ДОБАВЛЕНА ВОЗМНОЖНОСТЬ ПРОВЕДЕНИЯ ПЕРЕПИСКИ.
Запустить файл main.ipynb