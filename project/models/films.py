from project.database.connection import query


def get_all_films():
    sql = "SELECT * FROM t_film"
    films = query(sql, fetch='all')
    return films


def get_film_by_id(film_id):
    sql = "SELECT * FROM t_film WHERE id_film = %s"
    film = query(sql, fetch='one', values=film_id)
    return film


def add_genre_to_film(film_id, genre_id):
    sql = "INSERT INTO t_genre_film (`fk_genre`, `fk_film`) VALUES (%s, %s)"
    values = genre_id, film_id
    return query(sql, values=values)


def remove_genre_from_film(film_id, genre_id):
    sql = "DELETE FROM t_genre_film WHERE fk_film = %s AND fk_genre = %s;"
    values = film_id, genre_id
    return query(sql, values=values)


def get_genres_ids(id_film):
    sql = "SELECT g.id_genre " \
          "FROM t_genres AS g " \
          "LEFT JOIN t_genre_film AS tgf ON g.id_genre = tgf.fk_genre " \
          "LEFT JOIN t_film  AS f ON tgf.fk_film = f.id_film " \
          "WHERE id_film = %s;"

    genres = query(sql, fetch='all', values=id_film)

    ids_genres = []
    for genre in genres:
        ids_genres.append(str(genre['id_genre']))

    return ids_genres


def update_genres_from_film(film_id, new_genres_ids):
    old_genres_ids = get_genres_ids(film_id)

    remove_genres = list(set(old_genres_ids) - set(new_genres_ids))
    for id_genre in remove_genres:
        remove_genre_from_film(film_id, id_genre)

    add_genres = list(set(new_genres_ids) - set(old_genres_ids))
    for id_genre in add_genres:
        add_genre_to_film(film_id, id_genre)