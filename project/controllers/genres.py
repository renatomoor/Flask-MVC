from flask import render_template, request, redirect, url_for, flash
from project import app
from ..database.errors import if_error_show
from ..models import genres


@app.route('/genres')
def genres_list():
    genres_data = genres.get_all_genres()
    return render_template('genres/genres.html', genres=genres_data)


@app.route('/genre/add', methods=['GET', 'POST'])
def genre_add():
    if request.method == 'POST':
        genre_name = request.form['genre_name']
        try:
            genres.add_genre(genre_name)

        except Exception as error:
            if_error_show(error, 1062, 'Ce genre existe déjà', 'warning')
            return render_template('genres/addGenre.html')

        else:
            flash('Genre ajoutée', 'success')
            return redirect(url_for('genres_list'), code=302)

    return render_template('genres/addGenre.html')


@app.route('/genre/<id_genre>/delete')
def genre_delete(id_genre):
    genres.delete_genre(id_genre)
    return redirect(url_for('genres_list'), code=302)


@app.route('/genre/<id_genre>/edit', methods=['GET', 'POST'])
def genre_edit(id_genre):
    genre = genres.get_genre_by_id(id_genre)

    if request.method == 'POST':
        genre_name = request.form['genre_name']
        try:
            genres.edit_genre(id_genre, genre_name)

        except Exception as error:
            if_error_show(error, 1062, 'Ce genre existe déjà', 'warning')
            return render_template('genres/editGenre.html', genre=genre)

        else:
            flash('Genre editée', 'success')
            return redirect(url_for('genres_list'), code=302)

    return render_template('genres/editGenre.html', genre=genre)
