Résumé du Projet
Ce projet met en œuvre une architecture microservices utilisant Nginx comme serveur proxy pour deux applications Django distinctes, permettant une répartition efficace du trafic utilisateur. Grâce à la directive split_clients de Nginx, le système peut diriger le trafic en fonction d'un paramètre de requête, facilitant ainsi la réalisation de tests A/B et l'optimisation des performances des applications.

Fonctionnalités principales :

Équilibrage de charge : Le trafic est réparti entre deux applications Django (web1 et web2) selon une logique de répartition définie. Par exemple, 50% des requêtes peuvent être envoyées vers la première application, tandis que le reste va vers la seconde, ce qui permet de tester différentes versions ou configurations d'une application.
Gestion des fichiers statiques : Nginx gère les fichiers statiques, ce qui réduit la charge sur les serveurs d'application Django et améliore la performance.
Containerisation avec Docker : Le projet utilise Docker pour encapsuler les applications Django, Nginx et le service DNS, facilitant le déploiement et la gestion des dépendances.
Utilité

Ce projet est idéal pour les développeurs souhaitant tester différentes versions d'une application en temps réel, optimiser l'expérience utilisateur, et gérer efficacement le trafic sur leurs services web. L'utilisation de conteneurs Docker simplifie le déploiement et la maintenance de l'architecture, rendant le système facilement extensible et modulaire.