from fpdf import FPDF


class PDF(FPDF):
    def __init__(self, name):
        self._pdf = FPDF()
        self._pdf.add_page()
        self._pdf.set_font("Arial", size=40)
        self._pdf.cell(0, 60, "CS50 Shirtificate", new_x="LMARGIN", align="C")
        self._pdf.image("shirtificate.png", w=self._pdf.eph)
        self._pdf.set_font(30)
        self._pdf.set_text_color("blue")
        self._pdf.text(x=47.5, y=140, txt=f"{name} took CS50")

    def save(self, name):
        self._pdf.save


name = input("Nane: ")
pdf = PDF(name)
pdf.save("shirtificate.pdf")
