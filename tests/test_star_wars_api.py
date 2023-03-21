import allure
from utils.api import Star_wars_api

""" Создаем класс, в котором будем хранить шаги для теста """

"""Cохранение всех персонажей, которые снимались во всех фильмах, с Дарт Вейдером, в тестовый файл"""
@allure.epic("Test Suite Name: Test get actors")  # Если написать перед каждым классом (суит тестом), в отчете будет разделение от других классов
class Test_get_actors:

    @allure.description("Test get all actors")  # Перед каждым тестом будет описание этого теста
    def test_get_all_actors(self):
        print("\n --Начало работы кода, для поиска всех фильмом с Дарт Вейдером--\n")
        """В переменную result_post храним экземпляр класса Google_maps_api, из которой вызываем необходимый метод (метод create_new_place)"""
        result_get_vader = Star_wars_api.get_all_films_vader()  # Для поиска всех фильмов с участием "Darth Vader", обращаемся к методу get_all_films_vader,
        check_get_vader = result_get_vader.json()               # В переменную сохраняем ответ в формате json, для дальнейшей работы с ним
        films_vader = check_get_vader.get("films")              # Получаем значения поля "films"
        print("Список всех ссылок для поиска актеров: " + str(films_vader))

        print("\n --Начало работы кода, для поиска всех актеров--")
        for i in films_vader:                                           # Для всех ссылок создаем Get запрос
            result_get_url_actors = Star_wars_api.get_all_actors(i)     # Обращаемся к методу get_all_films_vader, для поиска url актеров по названию фильма
            check_get_url_actors = result_get_url_actors.json()         # В переменную сохраняем ответ в формате json, для дальнейшей работы с ним
            all_url_actors = check_get_url_actors.get('characters')     # Получаем значения поля "characters", где перечисленны url на актер
            print("Все ссылки для поиска актеров: ")
            print(all_url_actors)                                       # Список url для поиска актеров

            all_actors_file = open("doc/all_actors", "w", encoding="utf-8")  # Создаем файл в режиме "w", чтоб очистить содержимое перед каждым циклом
            for j in all_url_actors:                                   # Для всех ссылок создаем Get запрос
                result_get_actors = Star_wars_api.get_all_actors(j)    # Обращаемся к методу get_all_films_vader, для поиска актеров по url
                check_get_actors = result_get_actors.json()            # В переменную сохраняем ответ в формате json, для дальнейшей работы с ним
                all_actors = check_get_actors.get('name')              # Получаем значения поля "name", где перечисленны имена актер
                print(all_actors)                                      # Список актеров
                """Создание текстового файла для хранения всех персонажей, игравшие с Дарт Вейдером"""
                all_actors_file.write(all_actors + "\n")     # В файле сохраняем значение поля "name" (построчно)
            all_actors_file.close()
