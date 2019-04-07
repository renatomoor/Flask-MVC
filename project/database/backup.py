import os
import pipes
import time
import platform
import yaml

document = open('config.yml', 'r')
config = yaml.load(document, Loader=yaml.FullLoader)

# Set all variables
DB_HOST = config['database']['host']
DB_USER = config['database']['user']
DB_USER_PASSWORD = config['database']['password']
DB_NAME = config['database']['database']
BIN_PATH = config['database']['mysql_bin_path']

system = platform.system()
BACKUP_PATH = 'project/database/backup/'
CURRENTPATH = 'project/database/'

PATH_W = os.getcwd() + '\\'
PATH_N = os.getcwd() + '/'
BACKUP_PATH_W = 'project\\database\\backup\\'
CURRENTPATH_W = 'project\\database\\'

# Getting current DateTime to create the separate backup folder.
DATETIME = time.strftime('%Y-%m-%d--%H_%M_%S')

# create backup folder if not exist
try:
    os.stat(BACKUP_PATH)
except:
    os.mkdir(BACKUP_PATH)

if BIN_PATH == '':
    mysqldump = 'mysqldump'
else:
    if system != 'Windows':
        mysqldump = 'cd ' + BIN_PATH + ' && cd .. && bin/mysqldump'
    else:
        mysqldump = 'cd ' + BIN_PATH + ' && cd .. && bin\mysqldump'

if system != 'Windows':
    dumpcmd1 = mysqldump + " -h " + DB_HOST + " -u " + DB_USER + " -p" + DB_USER_PASSWORD + " --databases " + DB_NAME + " > " + pipes.quote(
        PATH_N + BACKUP_PATH) + DB_NAME + "--" + DATETIME + ".sql"
    dumpcmd2 = mysqldump + " -h " + DB_HOST + " -u " + DB_USER + " -p" + DB_USER_PASSWORD + " --databases " + DB_NAME + " > " + pipes.quote(
        PATH_N + CURRENTPATH) + "database.sql"
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
else:
    dumpcmd1 = mysqldump + " -h " + DB_HOST + " -u" + DB_USER + " -p" + DB_USER_PASSWORD + " --databases "\
               + DB_NAME + " > " + PATH_W + BACKUP_PATH_W + DB_NAME + "--" + DATETIME + ".sql"

    dumpcmd2 = mysqldump + " -h " + DB_HOST + " -u" + DB_USER + " -p" + DB_USER_PASSWORD + " --databases "\
               + DB_NAME + " > " + PATH_W + CURRENTPATH_W + "database.sql"
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
