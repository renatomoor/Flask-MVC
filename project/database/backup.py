import os
import pipes
import time
import platform
import yaml

document = open('config.yml', 'r')
config = yaml.load(document, Loader=yaml.FullLoader)

system = platform.system()
DB_HOST = config['database']['host']
DB_USER = config['database']['user']
DB_USER_PASSWORD = config['database']['password']
DB_NAME = config['database']['database']
BACKUP_PATH = 'project/database/backup/'
CURRENTPATH = 'project/database/'

# Getting current DateTime to create the separate backup folder like "20180817-123433".
DATETIME = time.strftime('%Y-%m-%d--%H:%M:%S')

# Checking if backup folder already exists or not. If not exists will create it.
try:
    os.stat(BACKUP_PATH)
except:
    os.mkdir(BACKUP_PATH)

if system != 'Windows':
    dumpcmd1 = "mysqldump -h " + DB_HOST + " -u " + DB_USER + " -p" + DB_USER_PASSWORD + " --databases " + DB_NAME + " > " + pipes.quote(
        BACKUP_PATH) + DB_NAME + "--" + DATETIME + ".sql"
    dumpcmd2 = "mysqldump -h " + DB_HOST + " -u " + DB_USER + " -p" + DB_USER_PASSWORD + " --databases " + DB_NAME + " > " + pipes.quote(
        CURRENTPATH) + "database.sql"
    try:
        os.system(dumpcmd1)
        os.system(dumpcmd2)
        print("")
        print("Backup script completed")
        print("Your backups have been created in '" + BACKUP_PATH + "' directory")

        print("Your database.sql have been updated in project/database/database.sql directory")
        print("Now you can restore your database with the command pipenv run mysql_restore ")
    except:
        print("ERROR -- impossible to create the backup")