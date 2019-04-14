from project.database.connection import query
from ..models import genres


def get_all_films():
    sql = "SELECT * FROM t_film"
    films = query(sql, fetch='all')
    return films


def get_film_by_id(id_film):
    sql = "SELECT * FROM t_film WHERE id_film = %s"
    film = query(sql, values=id_film, fetch='one')
    return film


def add_genre_to_film(id_film, id_genre):
    sql = "INSERT INTO t_genre_film (fk_genre, fk_film) VALUE (%s, %s)"
    values = id_genre, id_film
    return query(sql, values=values)


def remove_genre_from_film(id_film, id_genre):
    sql = "DELETE FROM t_genre_film WHERE fk_film = %s AND fk_genre = %s"
    values = id_film, id_genre
    return query(sql, values=values)


def update_genres_from_film(id_film, new_genres_ids):
    old_genres = genres.get_genres_by_film_id(id_film)
    old_genres = list(map(get_genre_id_from_genre, old_genres))

    add_genres = list(set(new_genres_ids) - set(old_genres))

    for id_genre in add_genres:
        add_genre_to_film(id_film, id_genre)

    remove_genres = list(set(old_genres) - set(new_genres_ids))
    for id_genre in remove_genres:
        remove_genre_from_film(id_film, id_genre)


def get_genre_id_from_genre(genre):
    return genre['id_genre']
