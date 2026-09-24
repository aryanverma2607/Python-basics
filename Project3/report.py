from reportlab.pdfgen import canvas
from Grammar import grammar_check
from Document import open_file,select_document

pdf = canvas.Canvas("Corrected.pdf")

pdf.drawString(50,800,text)
pdf.drawString(50,750,)

pdf.setFont("Courier",15)


