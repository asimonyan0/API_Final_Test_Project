from utils.http_methods import Http_methods

""" Можно собрать все методы (не только Star Wers) по api """

""" Метод для тестирования Star Wars API """
base_url = "https://swapi.dev/api/"   # Базовый url

class Star_wars_api:

    """ Метод для поиска всех фильмов с участием "Darth Vader" """
    @staticmethod     # Сделаем методы статическими (без Self) и сможем вызывать в любом классе и в любом тесте, и не будем привязываться к этому классу
    def get_all_films_vader():
        get_resource_vader = "people/4/"   # Ресурс для поиска всех фильмов с участием "Darth Vader"
        get_url_vader = base_url + get_resource_vader  # Полный ресурс для запроса get
        print("URL для фильмов с участием Darth Vader: " + get_url_vader)
        result_get = Http_methods.get(get_url_vader)   # Отправляем запрос по методу get из класса  Http_methods
        # print(result_get.text)                         # Печатаем результат в формате text
        return result_get                              # Возвращаем результат запроса

    """ Метод для поиска актеров по названию фильма """
    @staticmethod
    def get_all_actors(films_vader):
        get_url_actors = films_vader      # Полный ресурс для запроса get (поиска актеров по фильмам)
        print("\n--Поиск актера по ссылке: " + get_url_actors)
        result_get_actors = Http_methods.get(get_url_actors) # Отправляем запрос по методу get из класса  Http_methods
        # print(result_get_actors.text)                      # Печатаем результат в формате text
        return result_get_actors                             # Возвращаем результат запроса



