import yaml
import pymysql
import sqlparse

document = open('config/config.yml', 'r')
sql = open('project/database/database.sql', 'r')

config = yaml.load(document, Loader=yaml.FullLoader)


def init_database():
    try:

        db = pymysql.connect(host=config['database']['host'],
                             user=config['database']['user'],
                             password=config['database']['password'],
                             cursorclass=pymysql.cursors.DictCursor)

        cursor = db.cursor()
        stmts = sqlparse.split(sql.read())

        for stmt in stmts:
            cursor.execute(stmt)
        db.commit()
        print('All queries were executed successfully')
    except (
            pymysql.err.OperationalError, pymysql.ProgrammingError, pymysql.InternalError,
            pymysql.IntegrityError) as error:
        print('Exception number: {}, value {!r}'.format(error.args[0], error))
        raise
    else:
        cursor.close()
        db.close()


init_database()
