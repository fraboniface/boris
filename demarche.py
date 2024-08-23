from fasthtml.common import *
from utils import Markdown

t1 = 'Qui sommes-nous ?'
t2 = 'Pourquoi Boris ?'
t3 = 'Les grandes étapes du projets'

sec1 = """
Boris s'inscrit dans le cadre de la démarche beta.gouv.fr

Ce dispositif permet de créer une plateforme numérique avec la méthode Start-up d’État. 

L'équipe en charge du projet travaille sans préjuger du résultat final et se confronte constamment aux retours des utilisateurs. Ainsi, le service, imparfait au départ s'améliore de façon continuer.  Si vous voulez en savoir plus, n'hésitez pas à consulter notre fiche projet sur la plateforme beta.gouv.fr.

Vous constatez une erreur ? Vous avez un conseil ? N'hésitez pas à nous contacter grâce au formulaire en bas de cette page !  
"""

sec2 = """
En nommant ce projet BoRiS, nous cherchons à donner un visage au service que nous proposons autour du Bail Réel Solidaire. 

Vous l'aurez remarqué, BoRiS reprend les lettre du sigle BRS.
Mais c'est aussi un prénom, celui que nous avons donné à notre chatbot grâce auquel vous pouvez déterminer si vous êtes éligible ou non au dispositif. C'est le moyen que nous avons trouvé de le rendre plus "humain", comme si vous aviez quelqu'un à qui poser toutes vos questions sur ce dispositif qui n'est pas toujours simple à comprendre.
"""

sec3 = """
**Avril 2023** : Un agent public identifie un enjeu qui pourrait bénéficier de l'approche Startup d'État

**Juin-Août 2023 : Lancement de la phase d'investigation**

L'équipe du projet (1 intrapreneur + 1 coach) ont testé la pertinence du projet à travers des interviews d'une vingtaine de personnes (acheteurs en BRS, bénéficiaires potentiels, banques, OFS…) et des travaux de recherche.

**Août 2023 : Comité d'investissement**

À partir des conclusions de la phase d'investigation, le comité d'investissement a validé la pertinence du projet et l'entrée en phase de construction pour 6 à 8 mois.

**Septembre 2023 - Mai 2024 : Phase de construction**

Pendant 6 mois, nous testons l'idée en créant un prototype fonctionnel (notamment ce site web et le simulateur d'éligibilité). L'objectif est de tester auprès des futurs usagers la pertinence de la solution. 
Nous avons également associé à notre démarche 6 Organismes Fonciers Solidaires des régions Auvergne Rhône-Alpes et PACA. Nous avons à cœur d'intégrer tous les acteurs clefs du BRS à chaque étape de le démarche.
D'ici la phase de la construction, nous souhaitons améliorer cette plateforme avec vos retours et concevoir le dispositif de mise en relation entre les ménages qui recherchent un bien en BRS dans une ville spécifique et les programmes disponibles dans les quartiers correspondant.

**Et après ?**

Après un nouveau comité d'investissement qui clôturera la phase de construction, nous avons la ferme intention de développer cette plateforme pour répondre aux enjeux des ménages dans leur recherche d'un logement à prix abordable. Nous continuerons à ajouter des informations utiles aux acquéreurs à chaque étape de leur parcours.

Nous souhaitons également apporter un soutien aux propriétaires en BRS qui souhaitent revendre leur logement et se positionner en tiers de confiance.
"""

def page():
    sections = []
    for t, s in zip((t1, t2, t3), (sec1, sec2, sec3)):
        sections.append(Section(*(H2(t, style="text-align: center;"), Markdown(s), Br())))
    return Container(*sections)