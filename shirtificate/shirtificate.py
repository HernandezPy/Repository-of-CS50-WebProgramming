from fpdf import FPDF


class PDF(FPDF):
    def __init__(self, name):
        self.name = name
        self._pdf = FPDF(orientation="P", format="A4")
        self._pdf.add_page()
        self._pdf.set_font("Arial", "B", size=40)
        self._pdf.cell(0, 60, "CS50 Shirtificate", ln=True, align="C")
        self._pdf.image("shirtificate.png", x=15, y=60, w=180)
        self._pdf.set_font("Arial", "B", 25)
        self._pdf.set_text_color(255, 255, 255)
        self._pdf.

name = input("Name: ")
pdf = PDF(name)

