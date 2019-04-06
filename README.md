# Base MVC project with Flask
Ceci est une base pour commencer à construire votre propre projet MVC avec Flask, Jinja2, PyMySql et Bootstrap
### [Télécharger Flask-MVC](https://github.com/renatomoor/Flask-MVC/archive/master.zip)  

### Database:
Modifiez le fichier config.yml situé à `config.yml`

```yaml
database:
  host:      'localhost'               # Your host
  user:      'root'                    # Your database user
  password:  'XXXXXXXXX'               # Your database password
  database:   NOMPRENOMSUJET_BD_104_V1 # Your database name
  port:       3306                     # Your database port 
  mysql_path: '' #(OPTIONAL database backup) Only if you are using external applications for mysql as (MAMP, UwAmp, XAMPP...)
                 # With these we can do the backup of the database

server:
  address:  '0.0.0.0'                 # address to run your server Ex: 127.0.0.1 or 0.0.0.0
  port:     '8000'                    # port to run the server ex: 8080, 8000, 5000, 80, etc...
```


## Installer Environment:
###  1 - Installer pipenv
```
pip install pipenv
```
[Comment installer pipenv](https://geniesducode.com/articles/comment-installer-pipenv/)  
Python et pip sont nécessaires

###  2 - Install dependencies
```
pipenv install
```

###  3 - Restore database
```
pipenv run mysql_restore
```
Cette commande va exécuter le fichier `project/database/database.sql`

Si l'erreur  `pymysql.err.InternalError: (1065, 'Query was empty')` se produit
c'est parce que probablement vous avez un retour à la ligne à la fin votre ficher database.sql

### 4 - Lancer le serveur
```
pipenv run server
```

## Tools:

### 4 - Backup your database
**Il est nessesaire de specifier le chemin de votre mysql si le serveur mysql est un application externe tel que ( MAMP, UwAmp, XAMPP...)** dans `config.yml`  
```
pipenv run mysql_backup
```

Cette commande va sauvegarder l'état actuel de votre base de données dans el dossier `project/database/backup/`   
Elle va aussi récrire le ficher `project/database/database.sql` pour pouvoir aussi postérieurement utiliser la commande `pipenv run mysql_restore`  
#####External application mysql:   
Le chemin va dependre de votre logiciel serveur mysql, quelques examples:   
##### WINDOWS
 -  MAMP: `C:\MAMP\bin\mysql\bin`
 -  UwAmp `C:\UwAmp\bin\database\mysql-5.7.11\bin`
 
##### MAC
 -  MAMP: `/Applications/MAMP/Library/bin`

### -  Icônes:   [Fontawesome](https://fontawesome.com/icons?d=gallery)  free version
Example: 
``` 
<i class="fas fa-poo"> </i> 
```


### -  [Bootstrap](https://fontawesome.com/icons?d=gallery) v4.3.1
