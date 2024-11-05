Projet Docker Django et Nginx avec Serveur DNS

Ce projet met en place une application Django déployée avec Nginx comme reverse proxy et un serveur DNS avec BIND, tous configurés dans un environnement Docker. Cette configuration permet d’héberger l’application Django, de gérer le trafic avec Nginx, et de servir des requêtes DNS spécifiques.

Prérequis

Assurez-vous d’avoir les logiciels suivants installés :

Docker (pour la gestion des conteneurs)
Visual Studio Code avec l'extension Docker pour faciliter l’interaction avec les conteneurs
Structure de la configuration

Fichiers principaux

docker-compose.yml : Décrit les services et leur configuration.
Dockerfile (pour Nginx) : Personnalise l’image de Nginx avec un fichier HTML.
Configuration de zone DNS : Définie dans le dossier ./dns/zone/.

Configuration de docker-compose.yml

version: '3.8'

Services

web : Service Django utilisant Gunicorn.
context : Répertoire ./django/ où se trouve l'application Django.
command : Utilise Gunicorn pour exécuter l’application.
volumes : Monte le code source et les fichiers statiques.
expose : Expose le port 8000 pour les connexions internes.
env_file : Charge les variables d’environnement depuis .env/dev.env.
nginx : Service Nginx pour le reverse proxy.
context : Répertoire ./nginx/ avec les configurations spécifiques.
ports : Lie le port 80 du conteneur au port 80 de la machine hôte.
volumes : Monte les configurations Nginx et les fichiers statiques pour servir l’application.
dns : Service DNS avec BIND.
context : Répertoire ./dns/ avec les fichiers de configuration DNS.
ports : Expose le port 53 pour les requêtes DNS TCP et UDP.
volumes : Monte le fichier de configuration principal named.conf et les fichiers de zone.
command : Exécute BIND en mode frontal avec le fichier named.conf.
Volumes
static_files : Volume pour partager les fichiers statiques entre Nginx et Django.
Instructions d’installation et de déploiement

Étapes de configuration de Nginx
Télécharger l’image Nginx :

docker pull nginx
docker run -it --rm -d -p 8000:80 --name website nginx
Accéder à Nginx : Visitez http://localhost:8000 pour voir la page par défaut.
Accéder au terminal du conteneur : Dans l’extension Docker de Visual Studio Code, faites un clic droit sur le conteneur et sélectionnez Attach shell ou utilisez :

docker exec -it <container_id> bash
Tester Nginx :
nginx -v : Vérifie la version de Nginx.
nginx -t : Teste la configuration.
Configurer un fichier docker-compose.yml et Dockerfile pour Nginx : Créez un fichier Dockerfile :
dockerfile
Copier le code
FROM nginx:latest
COPY ./html/index.html /usr/share/nginx/html/index.html
Exemple de docker-compose.yml :


services:
  nginx:
    build:
      context: .
    ports:
      - 8000:80
    volumes:
      - ./html/:/usr/share/nginx/html/
Lancer les services :

docker-compose build
docker-compose up -d
Installation et configuration de Django
Installer Django et créer le projet :

python3 -m venv venv
source venv/bin/activate
pip install django
cd django
django-admin startproject demo .
python3 manage.py migrate
python3 manage.py createsuperuser  # Crée un administrateur
Configurer settings.py :

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = int(os.environ.get("DEBUG", default=0))
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", default="127.0.0.1").split(" ")
Créer une application Django :

python3 manage.py startapp demoapp
Démarrer Django avec Gunicorn : Modifiez docker-compose.yml pour que Django utilise Gunicorn :

command: gunicorn demo.wsgi:application --bind 0.0.0.0:8000
Configuration du DNS avec BIND
Configuration de BIND : Dans le répertoire ./dns/, créez un fichier named.conf et une zone dans zone/.
Exemple de fichier de zone DNS :
dns
Copier le code
$ttl 86400
@       IN      SOA main.com hostmaster.main.com. (
                    202 ; Serial
                    600 ; Refresh
                    3600 ; Retry
                    1209600 ; Expire
                    3600) ; Negative Cache TTL

@       IN      NS  main.com.
@       IN      A   127.0.0.1
www     IN      A   127.0.0.1
Vérifier le DNS :

nslookup ns.main.com 127.0.0.1
Commandes Docker utiles

Lancer les conteneurs : docker-compose up -d
Arrêter les conteneurs : docker-compose down
Reconstruction de l’image : docker-compose build
Nettoyer les volumes : docker volume rm $(docker volume ls -qf dangling=true)
Dépannage

Tester la configuration Nginx : nginx -t
Redémarrer BIND si des modifications sont apportées aux fichiers de zone : docker-compose restart dns
Licence

Ce projet est sous licence MIT.