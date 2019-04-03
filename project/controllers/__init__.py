import os
import glob
import yaml

document = open('config.yml', 'r')
config = yaml.load(document, Loader=yaml.FullLoader)

__all__ = [os.path.basename(
    f)[:-3] for f in glob.glob(os.path.dirname(__file__) + "/*.py")]
from project import app
from flask import flash, render_template
from ..database.errors import verify_error


@app.errorhandler(Exception)
def special_exception_handler(error):
    verify_error(error)
    flash(error, 'danger')
    return render_template('error.html', config=config, error=error)