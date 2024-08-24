## BoRiS en FastHTML

Ceci est une reproduction partielle du site [boris.beta.gouv.fr](https://boris.beta.gouv.fr/) faite avec [FastHTML](https://fastht.ml/), un nouveau framework permettant de créer des sites et applications web modernes en python uniquement. Le but était principalement de prendre en main ce nouveau framework, bien que je n'ai pas eu le temps d'en exploiter toutes les possibilités.

Elle est accessible à l'adresse suivante : [https://boris-6y20.onrender.com/simulateur](https://boris-6y20.onrender.com). Le serveur est déployé sur une instance gratuite, donc attendez-vous à un léger temps de chargement.

Dans le site tel quel, la seule différence avec un site statique (pur HTML/CSS) est visible sur le simulateur : cliquer sur Tester mon éligibilité ne recharge pas la page mais ajoute ou modifie directement le résultat présenté sous le formulaire, comme un site réactif. Le simulateur est factice : il vérifie simplement si Revenu du foyer / Taille du foyer < 25000.
