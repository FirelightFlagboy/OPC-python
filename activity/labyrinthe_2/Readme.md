# Labyrinthe

## Rule
- un `serveur` doit gerer le jeu
	- plusieur client peuvent etre present si la partie n'a pas commancer
- le jeu est en tour par tour
	- le robot ne fais que un mouvement, on peut toujour demander au robot
	d'aller 3 vers l'avant mais il ne ce deplacera que une fois par tour (il fait que une action par tour)
- on doit avoir des test unitaire
- le robot peut murer des portes ou percer les mur

### Controle du robot
| letter | action |
| --- | --- |
| `n` | deplace si possible le `robot` vers le `nord` |
| `s` | deplace si possible le `robot` vers le `sud` |
| `e` | deplace si possible le `robot` vers le `est` |
| `w` | deplace si possible le `robot` vers le `oues` |
| `m[n]` | le robot mure la porte dans la direction `n` |
| `p[n]` | le robot perce dans le mur dans la direction `n` |
| `c` | lance la partie si pas encore commencer |
### Affichage
- le `serveur` doit gerer les deplacement
- le `serveur` renvoie la map au client
- on doit pouvoir differencie le `Robot` qui peut ce deplacer des autres

### Fonctionnalités
- identique a celle de la premiere version
- il n'est pas utile d'enregistrer les partie

### Lancement
- serveur
	1. Le serveur est lancer en premier
	1. on choisi la carte
	1. les client se connecte
	1. une fois la partie demarer plus personne ne peut rejoindre
- client
	1. lancer apres que le serveur est choisi la carte
	1. un robot a créer et place aleatoirement sur la map (sur une case vide)
	1. on entre la commande `c` pour commencer la partie

### Client
- doit etre capable d'ecouter le serveur et de demander les commandes a l'utilisateur (threading)

### Evaluation
- on peut lancer le programme sans le modifier avec les fonctionnalite de l'exercice
- lisibilité du code
- decoupage du projet
- documentation
- pertinence des test
- ouverture a l'amelioration
