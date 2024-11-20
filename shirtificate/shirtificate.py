from fpdf import FPDF


def main():
    name_on_tshirt = input("Name: ")


def pdf_tshirt():
    pdf = FPDF(orientation="portrait", format="A4", width=210, height=297)
    pdf.add_page()
    pdf.image("shirtificate.png", alt_text="name_on_tshirt")
    pdf.set_font("helvetica", size=12)
    pdf.text(text="CS50 Shirtificate")
    pdf.output("shirtificate.pdf")


if __name__ == '__main__':
    main()
