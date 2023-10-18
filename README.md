# Testing_service

### Описание
Django проект - сервис проведения тестирования  
Простой сервис проведения тестирования по каким-либо темам. 
Через админку загружаются тесты с вариантами ответов, один или несколько вариантов должны быть правильными.  
Тесты группируются в наборы тестов, которые затем пользователь может проходить и видеть свой результат.
Функциональные части сервиса:
- Регистрация пользователей
- Аутентификация/авторизация пользователей
- Зарегистрированные пользователи могут проходить любой из тестовых наборов
- Последовательный ответ на все вопросы, каждый вопрос должен выводится на новой странице с отправкой формы
- После завершения тестирования выводится результат:  
1) количество правильных/неправильных ответов  
2) процент правильных ответов
- Результаты сохраняются. Если повторно зайти в тест, отобразиться прошлый результат.

### Технологии
Python 3.11
Django 4.1.7
### Запуск проекта в dev-режиме
- Установите и активируйте виртуальное окружение
- Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
``` 
- В папке с файлом manage.py выполните команду:
```
python3 manage.py runserver
```
#### Экран регистрации
![image](https://github.com/MikhailBogachev/PET_Django4_testing_service/assets/56482452/35681c04-b578-42e0-8bf5-7753edcbb012)
#### Экран входа
![image](https://github.com/MikhailBogachev/PET_Django4_testing_service/assets/56482452/582e60e7-f753-4801-825a-887778a8f844)
#### Главный экран
![image](https://github.com/MikhailBogachev/PET_Django4_testing_service/assets/56482452/4cbdb824-8e9f-4e73-afc1-636a1186d61c)
#### Экран теста
![image](https://github.com/MikhailBogachev/PET_Django4_testing_service/assets/56482452/e46d62b5-d7a7-4dbc-9096-6c67d1d16acd)
#### Экран вопроса 1
![image](https://github.com/MikhailBogachev/PET_Django4_testing_service/assets/56482452/b2197d25-9d28-427b-82f9-3703d6ae942b)
#### Экран вопроса 2
![image](https://github.com/MikhailBogachev/PET_Django4_testing_service/assets/56482452/0ce0c872-0b74-4ece-8285-6775399c1e6e)
#### Экран с результатами
![image](https://github.com/MikhailBogachev/PET_Django4_testing_service/assets/56482452/90c85876-107e-49ea-ade7-ab0f0d4556e6)






### Авторы
Богачев Михаил 
