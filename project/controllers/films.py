from project import app
from flask import render_template, flash
from project.models import films, genres


@app.route('/films')
def films_list():
    films_data = films.get_all_films()

    for film in films_data:
        film['genres'] = genres.get_genres_by_film_id(film['id_film'])

    return render_template('films/films.html', films=films_data)
