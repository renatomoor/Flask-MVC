from flask import render_template, flash, request, redirect, url_for
from project import app
from project.models import films, genres


@app.route('/films')
def films_list():
    films_data = films.get_all_films()

    for film in films_data:
        film['genres'] = genres.get_genres_by_film_id(film['id_film'])

    return render_template('films/films.html', films=films_data)


@app.route('/film/<id_film>/genres/edit', methods=['GET', 'POST'])
def edit_genres_from_film(id_film):
    film_data = films.get_film_by_id(id_film)
    film_genres_data = genres.get_genres_by_film_id(id_film)
    all_genres = genres.get_all_genres()

    for genre in all_genres:
        if genre in film_genres_data:
            genre['selected'] = True

    if request.method == 'POST':
        film_genres_selected = request.form.getlist('genres[]')
        film_genres_selected = list(map(int, film_genres_selected))
        films.update_genres_from_film(id_film, film_genres_selected)
        flash('les genres on été modifié', 'success')
        return redirect(url_for('films_list'), code=302)

    return render_template('films/edit_film_genres.html', film=film_data, genres=all_genres)
