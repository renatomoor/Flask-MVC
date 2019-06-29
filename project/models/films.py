from project.database.connection import query


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


def remove_all_genres_from_film(id_film):
    sql = "DELETE FROM t_genre_film WHERE fk_film = %s"
    return query(sql, values=id_film)


def update_genres_from_film(id_film, new_genres_ids):
    remove_all_genres_from_film(id_film)
    for id_genre in new_genres_ids:
        add_genre_to_film(id_film, id_genre)
