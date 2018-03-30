# server game mastering

  server game mastering pour contrôle différente partie d'un escape game.
  et connaître l’état physique des différente partie du jeux

  le server en question est héberge sur un Raspberry et communique avec les différente partie du jeux (énigme et trappe) en bus et gère les ouverture de deux porte en directe.

## déploiement

### lancement serveur
```
  export LANG=C.UTF-8
  export LC_ALL=C.UTF-8
  export FLASK_APP=app.py

  cd /home/pi/server_escape_game/app_led

  pidflask = flask run --host=0.0.0.0

  pidenigme = python3 gestion_enigme.py

```
il y a un service de cree sur la plateforme pour l'active il suffi de faire
```
  sudo service seerver_game start
```
#### les différente connexion

* **image de présentation**
![connexion pin Raspberry](./app_led/static/img/IMG_76511.jpg)

GPIO  | description
:-: |:-:
SDA1 | connexion arduino i2c (bus) transition donnée correspondance A4
SCL1 | connexion arduino i2c (bus) transition horloge correspondance A5
gpio06 | ouverture de la porte 1
gpio13 | ouverture de la porte 2
gnd | branchement branchement avec tout élément pour équilibre le courant


#### librairie
 - github.com/mlgd/gpio
