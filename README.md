# Customers API

## Stack utilisée

 - **MariaDB**  
 SGBD simple d'utilisation, pas besoin de plus pour ce projet.
 - **Adminer**  
 Interface nous permettant de réaliser des actions directement sur la BD.
 - **FastApi**  
 Framework Web python simple d'utilisation. Il nous permet de construire facilement des API et de fournir automatiquement une documentation publique. 
____
## Démarrage du projet
 1. Docker et Docker Compose doivent être installés, et le service docker démarré
 1. Se positionner à la racine du projet :
 ```sh
docker-compose up
 ```
 3. Le projet est lancé en local [ici](http://localhost:5000/docs)
 3. Si ce n'est pas déjà fait, il faut [initialiser la BD](http://localhost/init/customers)
 3. Vous pouvez aussi vous connecter à l'interface [Adminer](http://localhost:8080/) avec les données ci-dessous :

| Clé      |   Valeur   |
| :------- | :--------: |
| System   |   MySQL    |
| Server   |  mariadb   |
| Username |    root    |
| Password |    root    |
| Database | mydatabase |

 6. Lien vers la [documentation](http://localhost:5000/docs) de l'API
 ___
 _/!\ Les erreurs SQL ne sont pas gérées !_

 [Documentaion de l'API](api_doc.pdf)