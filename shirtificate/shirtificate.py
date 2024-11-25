from fpdf import FPDF


class PDF(FPDF):
    def __init__(self, name):
        self._pdf = FPDF(orientation="P", format="A4")
        self._pdf.add_page()
        self._pdf.set_font("Arial", "B", size=20)
        self._pdf.cell(0, 20, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")
        self._pdf.image("shirtificate.png", w=self._pdf.epw)
        self._pdf.set_font_size(23)
        self._pdf.set_text_color(255, 255, 255)
        self._pdf.text(x=40, y=70, txt=f"{name} took CS50")
        self._pdf.output("shirtificate.pdf")

name = input("Name: ")
pdf = PDF(name)

