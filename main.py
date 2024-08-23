from fasthtml.common import *

from utils import Markdown
import demarche, info

# css = Style(":root, { --pico-font-size: 100%; --pico-font-family: Pacifico, cursive;}")
app, rt = fast_app(live=true, pico=True)

def navlink(title, href):
    return A(title, href=href, style="color: grey; decoration: none; color-hover: blue; decoration-current: underline;")

def nav():
    return Nav(
        Ul(Li(navlink("BoRiS", href="/"))),
        Ul(
            Li(navlink("Notre démarche", href="notre-demarche")),
            Li(navlink("Tout savoir sur le BRS", href="info-brs")),
            Li(navlink(Button("Simuler mon éligibiltié"), href="/simulateur")),
        ),
        style="margin: 10px 30px;",
    )


def footer():
    return Footer("Pied de page", style='text-align: center;')


def Page(title, *content):
    return Title(title), nav(), *content, footer()


@app.get("/")
def home():
    return Page("BoRiS - L'assistant du Bail Réel Solidaire",
        Header(
            Container(
            Grid(
                Container(
                    H1("BoRiS", style="font-size: 5rem"),
                    H3(
                        "La plateforme d'information et de simulation du bail réel solidaire",
                        style="font-family: Space Mono, monospace",
                    ),
                ),
                Img(src="assets/image.svg"),
            )
        )),
        Section(
            Container(
                H2("Le Bail Réel Solidaire ?"),
                Grid(
                    Markdown("""
Le bail réel solidaire (BRS) est un dispositif d’accession sociale à la propriété. Il permet à des ménages  sous plafond de ressources de devenir propriétaire d’un logement et ce, à un prix abordable.

Le principe du bail réel solidaire (BRS) repose sur la dissociation du foncier et du bâti : vous achetez uniquement le logement tandis qu'un Organisme de Foncier Solidaire (OFS) agréé par l'Etat garde la propriété du terrain. 

"""),
                    Markdown("""
Vous n’achetez donc que la partie bâtie du logement, ce qui représente entre 30 % à 50 % d’économie lors de l'achat. 

En contrepartie, vous vous engagez à vivre dans votre logement au titre de votre résidence principale.

Vous devez par ailleurs vous acquitter une faible redevance mensuelle auprès de l'OFS.
"""),
                ),
                Div(
                    A(
                        Button("Tout connaître sur le Bail Réel Solidaire"),
                        href="info-brs",
                    ),
                    style="text-align: center;",
                ),
            ),
            style="background-color: rgb(70, 95, 157); padding: 20px 0;",
        ),
    )


@app.get("/notre-demarche")
def get_demarche():
    return Page("Notre démarche", demarche.page())


@app.get("/info-brs")
def infos():
    return Page("Tout savoir sur le Bail Réel Solidaire", Main(
        info.page()
    ))

@app.get("/simulateur")
def simu():
    return Title("Simulateur d'éligibilité"), nav(), Container(
        P('A faire')
    )


serve()
