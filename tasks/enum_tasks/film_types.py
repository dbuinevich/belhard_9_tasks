"""
Написать класс FilmTypes, который будет наследоваться от Enum и содержать
константы-названия жанров фильмов.
"""
from enum import Enum


class FilmTypes(Enum):
    ACTION = 1
    COMEDY = 2
    DRAMA = 3
    FANTASY = 4
    HORROR = 5
    MYSTERY = 6
    ROMANCE = 7
    THRILLER = 8
    WESTERN = 9
