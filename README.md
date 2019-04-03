# Base MVC project with Flask
Ceci est une base pour commencer à construire votre propre projet MVC avec Flask, Jinja2, PyMySql et Bootstrap

### Database:
Modifiez le fichier config.yml situé à `condig/config.yml`

```yaml
database:
  host:     'localhost'               # Your host
  user:     'root'                    # Your database user
  password: 'XXXXXXXXX'               # Your database password
  database:  NOMPRENOMSUJET_BD_104_V1 # Your database name

server:
  address:  '0.0.0.0'   # address to run your server Ex: 127.0.0.1 or 0.0.0.0
  port:     '80'        # port to run the server ex: 8080, 8000, 5000, 80, etc...
```

## Environment:
### Installer pipenv
```
pip install pipenv
```
[Comment installer pipenv](https://geniesducode.com/articles/comment-installer-pipenv/)  
Python et pip sont nécessaires

### Install dependencies
```
pipenv install
```

### Create database
```
pipenv run mysql_reset
```
This command will execute the file `project/database/database.sql`

Si l'erreur  `pymysql.err.InternalError: (1065, 'Query was empty')` se produit
c'est parce que vous avez un retour à la ligne **à la fin** votre dicher .sql

## Lancer le serveur
```
pivenv run server
```

## Tools:

## -  Icônes:   [Fontawesome](https://fontawesome.com/icons?d=gallery)  free version
Example: 
``` 
<i class="fas fa-poo"> </i> 
```


### -  [Bootstrap](https://fontawesome.com/icons?d=gallery) v4.3.1