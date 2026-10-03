from reportlab.platypus import Paragraph,SimpleDocTemplate,Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(character,words,lines,sentence,text,check,correct,path):
    pdf = SimpleDocTemplate(path)
    styles = getSampleStyleSheet()
    story=[]  #in platypus all content is stored in list
    styles["Title"].fontName="Courier-Bold"
    story.append(Paragraph("ANALYSIS  HISTORY",styles["Title"]))
    story.append(Spacer(1,10))
    styles["Heading1"].fontName="Courier-bold"
    story.append(Paragraph("Original Document :",styles["Heading1"]))
    story.append(Spacer(1,5))
    story.append(Paragraph(str(text),styles["Normal"]))

    story.append(Spacer(1,20))
    story.append(Paragraph("Analysis Report :",styles["Heading1"]))
    story.append(Paragraph("Character Count :" + str(character)))
    story.append(Paragraph("Word Count :" + str(words)))
    story.append(Paragraph("Line Count :" + str(lines)))
    story.append(Paragraph("Sentence Count :" + str(sentence)))
    story.append(Paragraph("Grammar Error:" + str(len(check))))

    story.append(Spacer(1,20))
    story.append(Paragraph("Error Details: ",styles["Heading1"]))
    for i,r in enumerate(check,start=1):
        story.append(Paragraph(f"Error {i} :",styles["Normal"]))
        story.append(Paragraph("Type :" + str(r["category"]),styles["Normal"]))
        story.append(Paragraph("Problem :" + str (r["message"]),styles["Normal"]))
        story.append(Paragraph("Suggestion :" + ", ".join(r["replacements"]),styles["Normal"]))
        story.append(Spacer(1,10))
    story.append(Spacer(1,10))
    story.append(Paragraph("Corrected Document :",styles["Heading1"]))
    story.append(Spacer(1,10))
    story.append(Paragraph(str(correct),styles["Normal"]))
    pdf.build(story)



