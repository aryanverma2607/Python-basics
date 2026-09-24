# Report lab is a python library that mainly used to create PDF files and to format files
# user-defined module require installaltion
from reportlab.pdfgen import canvas

# to create basic PDF

pdf = canvas.Canvas("Demo.pdf")


pdf.drawString(100,750,"Hello Aryan! how are you??")
# PDF mein text likhne ke liye drwastring(x,y,Text) x=coordinate from top
# y= coordinate from bottom and text is what we want to write
pdf.drawString(100,600,"Python is considered both a compiled and an interpreted language.")

# to change font
pdf.setFont("Courier",32)  #setfont(font_name,font_size)
pdf.drawString(100,570,"Heyy")
'''
Common fonts:
Helvetica
Times-Roman
Courier
'''
#text color

from reportlab.lib import colors

pdf.setFillColor(colors.yellow)
pdf.drawString(100,500,"Yellow Text")

'''
Common Colors:
colors.red
colors.blue
colors.green
colors.black
colors.white
colors.yellow'''

# Bold/italic/bold+italic
# pdf.setFont("Times-Roman-Bold",36)   #Bold
# pdf.setFont("Times-Roman-Oblique",36)     #italic
pdf.setFont("Courier-BoldOblique",36)   #bold+oblique

#drawCenteredString()

pdf.drawCentredString(200,400,"Student Data")
'''
Useful methods:
drawString()         → left aligned
drawCentredString()  → center aligned
drawRightString()    → right aligned'''

#to draw lines,rectangle,circle
pdf.line(200,250,350,450)            #line(x1,y1,x2,y2)  coordinates(x1,y1) and (x2,y2)

pdf.rect(100,300,300,100)      #(x,y,width,height)   x,y=coordinate

pdf.circle(300,100,50)         #(x,y,radius)

# for next page

pdf.showPage()    #it is used to get new page

pdf.drawString(200,500,"Second page")   #same to add content to the new page

pdf.save()             #it save the pdf