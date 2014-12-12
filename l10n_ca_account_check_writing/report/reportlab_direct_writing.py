# *-* coding: utf-8 *-*
import os

from reportlab.lib.units import mm
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import letter

from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import (
    Frame, Paragraph, Table,
)

from reportlab.pdfbase.pdfmetrics import getFont


AREAS = {
    "Address": (22, 206, 145, 32),
    "SumLetter": (22, 240, 145, 8),
    "SumDigit": (177, 241, 30, 12),
    "Date": (167, 259, 41, 12),

    "Stub1": (8, 100, 200, 90),
    "Stub2": (9, 0, 200, 90),
}

DATA = {
    "Address": """
        Vincent Vinet
        123 Fake St
        North Pole, QC H0H 0H0
    """,
    "SumLetter": "One million dollars!",
    "SumDigit": "1000000.00",
    "Date": "2014-12-12",
    "Stub1": "",
    "Stub2": "",
}

STUB_W = [27, 62, 28, 28, 20, 26]



STUB_DATA = [
    (u"Date d'échéance", u"Facture", u"Montant Original",
        u"Balance", u"Réduction", u"Paiement"),
    ("2014-11-29", "120322", "115.00", "115.00", "", "115.00"),
    ("2014-11-29", "321", "-34.50", "-34.50", "", "-34.50"),
    (u"Montant du chèque", "", "", "", "", "80.50"),
]

STUB_STYLE = [
    ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
    ('SPAN', (0, -1), (4, -1)),
]

PARA_STYLES = {}
PARA_STYLES["Default"] = _PD = ParagraphStyle("Default", fontName="Helvetica", alignment="LEFT")
PARA_STYLES["Date"] = ParagraphStyle("Date", _PD, fontSize=11.0, leading=14.0)
PARA_STYLES["SumLetter"] = ParagraphStyle("SumLetter", _PD, fontSize=11.0, leading=14)
def main(debug=False):
    check = Canvas("Check.pdf", pagesize=letter)

    for key, (x, y, w, h) in AREAS.iteritems():
        x, y, w, h = map(mm.__mul__, (x, y, w, h))
        f = Frame(x, y, w, h, 0, 0, 0, 0, key, bool(debug))
        x1, y1 = x, y + h
        if key.startswith("Stub"):
            t = Table(STUB_DATA,
                      colWidths=map(mm.__mul__, STUB_W),
                      style=STUB_STYLE)
            f.addFromList([t], check)

        else:
            style = ParagraphStyle(key)
            if key == "Address":
                paragraphs = [
                    Paragraph(data, style) for data in DATA[key].split("\n")
                ]
            elif key == "SumLetter":
                data = DATA[key]
                font = getFont(style.fontName)
                fontsize = style.fontSize
                fill_len = 1
                fill = "{0:*>{1}}"
                while font.stringWidth(
                        fill.format(u" ", fill_len) + data,
                        fontsize) < w - 10:
                    fill_len += 1


                p = Paragraph(fill.format(u" ", fill_len) + data, style)
                paragraphs = [p]
            else:
                paragraphs = [Paragraph(DATA[key], style)]


            f.addFromList(paragraphs, check)

    check.showPage()
    check.save()

try:
    main(True)
except Exception, e:
    print e
    import pdb
    pdb.post_mortem()
else:
    os.system("xdg-open Check.pdf")
