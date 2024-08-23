from fasthtml.common import *
from markdown import markdown


md_exts = "codehilite", "smarty", "extra", "sane_lists"


def Markdown(s, exts=md_exts, **kw):
    return Div(NotStr(markdown(s, extensions=exts)), **kw)


def footer():
    return Footer("Pied de page", style='text-align: center;')


def Page(title, *content):
    return Title(title), nav(), *content, footer()
