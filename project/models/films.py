from project.database.connection import query


def get_all_films():
    sql = "SELECT * FROM t_film"
    films = query(sql, fetch='all')
    return films
