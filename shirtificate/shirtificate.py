from fpdf import FPDF


class PDF(FPDF):
    def __init__(self, name):
        self._pdf = FPDF()
        self._pdf.add_page()
        self._pdf.set_font("Arial", "B", size=40)
        self._pdf.cell(0, 60, "CS50 Shirtificate", new_x="LMARGIN", align="C")
        self._pdf.image("shirtificate.png", w=self._pdf.eph)
        self._pdf.set_font_size(30)
        self._pdf.set_text_color(255, 255, 255)
        self._pdf.text(x=47.5, y=140, txt=f"{name} took CS50")

    def save(self, name):
        self._pdf.output(name)

name = input("Nane: ")
pdf = PDF(name)
pdf.save("shirtificate.pdf")
