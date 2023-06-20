from typing import Union


class MapExercise:
    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        """
        !!Задание нужно решить используя map!!
        Посчитать средний рейтинг фильмов (rating_kinopoisk) у которых две или больше стран.
        Фильмы у которых рейтинг не задан или равен 0 не учитывать в расчете среднего.

        :param list_of_movies: Список фильмов.
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :return: Средний рейтинг фильмов у которых две или больше стран
        """
        pass
        ratings = list(map(MapExercise.get_ratings, list_of_movies))
        ratings_sum, movies_count = MapExercise.calculate_ratings(ratings)
        return ratings_sum / movies_count

    @staticmethod
    def get_ratings(movie: dict) -> list:
        if not movie["rating_kinopoisk"]:
            return 0
        if len(movie["country"].split(",")) >= 2 and float(movie["rating_kinopoisk"]) > 0:
            return float(movie["rating_kinopoisk"])
        else:
            return 0

    @staticmethod
    def calculate_ratings(ratings: list[float]) -> tuple:
        movies_count = 0
        rating_sum = 0
        for i in ratings:
            if i != 0:
                movies_count += 1
                rating_sum += i
            else:
                continue
        return (rating_sum, movies_count)

    @staticmethod
    def chars_count(list_of_movies: list[dict], rating: Union[float, int]) -> int:
        """
        !!Задание нужно решить используя map!!
        Посчитать количество букв 'и' в названиях всех фильмов с рейтингом (rating_kinopoisk) больше
        или равным заданному значению

        :param list_of_movies: Список фильмов
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :param rating: Заданный рейтинг
        :return: Количество букв 'и' в названиях всех фильмов с рейтингом больше
        или равным заданному значению
        """
        pass
        a = list(map(lambda mov: MapExercise.get_movies(mov, rating), list_of_movies))
        result = 0
        for i in a:
            if not i:
                continue
            else:
                result += i.count("и")
        return result

    @staticmethod
    def get_movies(movie: dict, rating: Union[float, int]) -> list:
        if not movie["rating_kinopoisk"]:
            return False
        if float(movie["rating_kinopoisk"]) >= rating:
            return movie["name"]
        else:
            return False
