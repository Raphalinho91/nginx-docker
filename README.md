Résumé de la Configuration Nginx
Cette configuration Nginx met en œuvre un système de limitation de débit pour contrôler le flux des requêtes entrantes sur le serveur. Les points clés de cette configuration sont les suivants :

Zone de Limitation de Requête :
La directive limit_req_zone $binary_remote_addr zone=limitbyaddr:10m rate=1r/s; définit une zone de limitation basée sur l'adresse IP des clients (représentée par $binary_remote_addr). Cette zone, nommée limitbyaddr, alloue 10 Mo de mémoire pour stocker les informations de limitation et limite chaque client à 1 requête par seconde.
État de Limitation :
La directive limit_req_status 429; spécifie que lorsqu'un client dépasse la limite de requêtes, le serveur renvoie un code d'erreur HTTP 429 (Trop de requêtes).
Serveur Upstream :
Le bloc upstream demo définit un groupe de serveurs, ici nommé demo, qui redirige les requêtes vers un serveur backend écoutant sur le port 8000.
Configuration du Serveur :
Le serveur écoute sur le port 80 et applique la limitation de requêtes avec limit_req zone=limitbyaddr burst=10 delay=5;. Cela permet un maximum de 10 requêtes à la fois, avec un délai de 5 secondes avant que les requêtes supplémentaires ne soient traitées.
Gestion des Requêtes :
Dans la localisation racine (location /), les requêtes sont proxy-passées au groupe de serveurs demo, en ajoutant les en-têtes nécessaires pour la traçabilité de la requête (X-Forwarded-For et Host).
La localisation /static/ est configurée pour servir des fichiers statiques depuis le chemin /home/app/staticfiles/.
Utilité de cette Configuration
Cette configuration est essentielle pour améliorer la résilience du serveur contre les abus et les attaques par déni de service (DoS) en limitant le nombre de requêtes qu'un client peut envoyer dans un laps de temps donné. Cela aide à préserver les ressources du serveur et à assurer une expérience utilisateur optimale en évitant la surcharge du backend. De plus, la gestion des fichiers statiques permet de décharger le serveur d'applications en servant efficacement le contenu statique.