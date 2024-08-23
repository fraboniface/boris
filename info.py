from fasthtml.common import *
from utils import Markdown


t1 = "Qu'est-ce que le Bail réel solidaire ?"
t2 = "Tout savoir sur le Bail Réel Solidaire - BRS "

s1 = """
Le Bail Réel Solidaire (BRS) est un dispositif mis en place par l’État permettant à des ménages qui ne pourraient pas devenir propriétaires d'un logement au prix du marché d’accéder à la propriété de leur résidence principale. 

En effet, les logements mis en vente en BRS sont 30 à 50% moins chers que ceux mis en vente dans le marché traditionnel. Les prix sont encadrés et contrôlés par l'État. Cela est rendu possible notamment parce que les propriétaires d'un logement en BRS achètent leur logement à 100%, mais pas le terrain sur lequel celui-ci est construit. En échange, les propriétaires d'un logement d'un BRS s'acquittent d'une redevance mensuelle contenue.

En tant que propriétaire d'un logement en BRS, vous disposez de tous les droits d'un·e propriétaire, et pouvez notamment revendre votre logement (avec une plus-value toutefois encadrée) ou le transmettre à vos proches. Le dispositif se veut ainsi solidaire car il permet aux générations futures d'accéder à la propriété dans des conditions similaires, de manière abordable. 

Le BRS existe depuis 2017 et les acquéreurs sont accompagnés tout au long de leur procédure d'achat par un organisme dédié. 
"""


def sec1():
    return Section(H1(t1), Markdown(s1))


def step(img_src, title, desc):
    return Div(
        Img(src=img_src, style="border-radius: 10px;"),
        Br(),
        Br(),
        H3(title),
        P(desc),
        style="margin: 10px 10px; max-width: 300px; flex: 1 1 100%;",
    )


steps = [
    (
        "assets/step1.jpg",
        "Etape 1 : Je me renseigne",
        "Découvrez les informations relatives au Bail Réel solidaire et testez votre éligibilité",
    ),
    (
        "assets/step2.jpg",
        "Etape 2 : Je trouve mon logement",
        "Trouvez le logement de vos rêves en BRS et candidatez pour l'obtenir",
    ),
    (
        "assets/step3.jpg",
        "Étape 3 : Je cherche des financements",
        "Assurez-vous de pouvoir financer votre achat grâce à vos fonds propres, un emprunt bancaire et des aides éventuelles",
    ),
    (
        "assets/step4.jpg",
        "Étape 4 : Je deviens propriétaire",
        "Une fois tous les éléments finalisés, vous pouvez signer l'acte de vente chez le notaire.",
    ),
    (
        "assets/step5.jpg",
        "Étape 5 : Je suis chez moi !",
        "Profitez de votre logement et assurez-vous de bien connaître les spécificités liées au BRS.",
    ),
]


def get_steps():
    l = [step(*s) for s in steps]
    return Container(
        l[0],
        l[1],
        l[2],
        l[3],
        l[4],
        style="display: flex; flex-wrap: wrap; gap: 1rem; justify-content: center;",
    )


faq1 = [
    ("Quels sont les avantages du BRS ?", "Réponse 1"),
    ("Quelles sont les contreparties ?", "Réponse 2"),
    ("Est-ce que j'ai accès à ce dispositif ?", "Réponse 3"),
]


def step1_detail():
    return Section(
        H1(steps[0][1]),
        *[
            Details(Summary(t[0], role="button", cls="secondary"), P(t[1]))
            for t in faq1
        ],
    )


def page():
    return Container(sec1(), Br(), Section(H1(t2), get_steps()), step1_detail())
