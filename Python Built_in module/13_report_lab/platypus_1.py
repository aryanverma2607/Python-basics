'''
from reportlab.platypus import SimpleDocTemplate, Paragraph
PDF document:
pdf = SimpleDocTemplate("Demo.pdf")
Ab ek story banate hain:
story = []
Story ka matlab:

PDF mein jo bhi content add karna hai, uska sequence.
Then:
story.append(Paragraph("Hello Aryan!"))
Finally:
pdf.build(story)
Complete flow
SimpleDocTemplate
       ↓
     story
       ↓
   Paragraph
       ↓
   story.append()
       ↓
   pdf.build()
       ↓
    Demo.pdf
2. Paragraph

Normal canvas mein:

pdf.drawString(100, 750, "Hello")

Platypus mein:

Paragraph("Hello")

Paragraph automatically available space ke according text arrange karta hai.

Long text bhi automatically next line mein chala jayega. 🔥

3. Style

Paragraph ko formatting dene ke liye:

from reportlab.lib.styles import getSampleStyleSheet

Then:

styles = getSampleStyleSheet()

Isme already kuch predefined styles mil jaate hain.

Example:

story.append(
    Paragraph("Student Information", styles["Title"])
)

Other common styles:

Title
Heading1
Heading2
Heading3
BodyText
4. Spacer

Do elements ke beech gap chahiye to:

from reportlab.platypus import Spacer

Then:

story.append(Spacer(1, 20))

Meaning:

Spacer(width, height)

Example:

Heading
   ↓
20 points gap
   ↓
Paragraph
5. Multiple Paragraphs
story.append(Paragraph("Student Information", styles["Title"]))

story.append(Spacer(1, 20))

story.append(Paragraph(
    "Aryan is a B.Tech CSE student.",
    styles["BodyText"]
))

Platypus khud decide karega ki content page par kaha place karna hai.

6. Table ⭐

Professional PDF mein tables ke liye:

from reportlab.platypus import Table

Data:

data = [
    ["Name", "Age", "Course"],
    ["Aryan", "20", "CSE"],
    ["Rahul", "21", "CSE"]
]

Table:

table = Table(data)

Then story mein:

story.append(table)
7. TableStyle

Table ko formatting dene ke liye:

from reportlab.platypus import TableStyle
from reportlab.lib import colors

Example:

table.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), colors.blue),
    ("TEXTCOLOR", (0,0), (-1,0), colors.white),
    ("GRID", (0,0), (-1,-1), 1, colors.black)
]))

Yahan:

BACKGROUND → background color
TEXTCOLOR  → text color
GRID       → table borders
8. PageBreak

Agar manually new page chahiye:

from reportlab.platypus import PageBreak

Then:

story.append(PageBreak())

Flow:

Page 1 content
      ↓
 PageBreak
      ↓
Page 2 content
9. Image

Platypus mein image bhi add kar sakte hain:

from reportlab.platypus import Image
img = Image("photo.jpg")
story.append(img)

Size control:

img = Image("photo.jpg", width=200, height=150)
🧠 Platypus ke Main Components

Ye important list yaad rakh:

Component	Use
SimpleDocTemplate	PDF document
Paragraph	Text/paragraph
Spacer	Gap
Table	Table
TableStyle	Table formatting
Image	Image
PageBreak	New page
KeepTogether	Elements ko saath rakhna
PageTemplate	Custom page layout
Frame	Content area
BaseDocTemplate	Advanced document control
NextPageTemplate	Different page templates
CondPageBreak	Conditional page break
'''