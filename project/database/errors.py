from flask import flash


def verify_error(error):
    if error.args:
        if error.args[0] == 1451:
            flash('La valeur que vous essayez de suprimer est déjà liee a une autre table', 'danger ')

        if error.args[0] == 1062:
            flash('Cette valeur existe déjà dans ce table', 'warning')

        if error.args[0] == 1064:
            flash('Vérifier les donnés introduits (C\'est une possibilité)', 'warning')


def if_error_show(error, error_number, message, type):
    if error.args[0] == error_number:
        flash(message, type)
