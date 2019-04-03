import inspect
import pymysql
import pymysql.cursors
import yaml
from flask import g

document = open('config.yml', 'r')
config = yaml.load(document, Loader=yaml.FullLoader)


def get_connection():
    if "db" not in g:
        try:
            g.db = pymysql.connect(host=config['database']['host'],
                                   user=config['database']['user'],
                                   password=config['database']['password'],
                                   db=config['database']['database'],
                                   cursorclass=pymysql.cursors.DictCursor)

        except (pymysql.err.OperationalError,
                pymysql.ProgrammingError,
                pymysql.InternalError,
                pymysql.IntegrityError,
                TypeError) as error:
            print("BD NON CONNECTEE, Il y a une ERREUR : %s", error)
            print('Exception number: {}, value {!r}'.format(error.args[0], error))
            raise
    return g.db


def close_connection():
    db = g.pop("db", None)
    if db is not None:
        db.close()


def query(sql, values=None, fetch=None):
    conn = get_connection()
    cursor = conn.cursor()
    result = []
    try:
        if values:
            cursor.execute(sql, values)
        else:
            cursor.execute(sql)

        if fetch == 'all':
            result = cursor.fetchall()

        if fetch == 'one':
            result = cursor.fetchone()
        conn.commit()

    except (pymysql.err.OperationalError,
            pymysql.ProgrammingError,
            pymysql.InternalError,
            pymysql.IntegrityError) as error:
        error.sql = sql
        if values:
            error.sql_values = values
            error.sql_with_values = sql % values
        if fetch:
            error.sql_fetch = fetch

        error.model_path = print_caller_info()

        conn.rollback()
        raise error

    finally:
        cursor.close()

    return result


def init_app(app):
    app.teardown_appcontext(close_connection)


def print_caller_info():
    stack = inspect.stack()
    previous_stack_frame = stack[2]
    calling_module = inspect.getmodule(previous_stack_frame[0])
    result = {}
    result['function'] = previous_stack_frame.function
    result['code_context'] = previous_stack_frame.code_context
    result['line'] = previous_stack_frame.lineno
    result['file'] = calling_module.__file__
    return result
