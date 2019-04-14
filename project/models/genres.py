from project.database.connection import query


def get_all_genres():
    sql = "SELECT * FROM t_genres"
    all_genres = query(sql, fetch='all')
    return all_genres


def get_genre_by_id(id_genre):
    sql = "SELECT * FROM t_genres WHERE id_genre = %s"
    genre = query(sql, fetch='one', values=id_genre)
    return genre


def add_genre(intitule_genre):
    sql = "INSERT INTO t_genres (intitule_genre) VALUES (%s)"
    query(sql, values=intitule_genre)


def edit_genre(id_genre, intitule_genre):
    sql = "UPDATE t_genres as g SET g.intitule_genre = %s WHERE g.id_genre = %s"
    values = intitule_genre, id_genre
    return query(sql, values=values)


def delete_genre(id_genre):
    sql = "DELETE FROM t_genres WHERE id_genre = %s"
    return query(sql, values=id_genre)


def get_genres_by_film_id(id_film):
    sql = "SELECT g.* " \
          "FROM t_genres AS g " \
          "LEFT JOIN t_genre_film AS tgf ON g.id_genre = tgf.fk_genre " \
          "LEFT JOIN t_film  AS f ON tgf.fk_film = f.id_film " \
          "WHERE id_film = %s;"
    return query(sql, fetch='all', values=id_film)
