from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv('topics.csv')

y_start = 21 # The starting y position for the lines

for index, row in df.iterrows():
    pdf.add_page()
    # Set the header for the main pages
    pdf.set_font('Times', style="B", size=24)
    pdf.set_text_color(100, 100, 254)
    pdf.cell(w=0, h=16, txt=row['Topic'], align='L', ln=1)
    
    # Draw the lines
    for y in range(21, 285, 10):
        pdf.line(x1=10, y1=y, x2=200, y2=y)

    # Set the footer for main pages
    pdf.ln(260)
    pdf.set_font('Times', style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row['Topic'], align='R')

    for i in range(row['Pages'] - 1):
        pdf.add_page()
        # Set the footer for other pages
        pdf.ln(276)
        pdf.set_font('Times', style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row['Topic'], align='R')

        # Draw the lines
        for y in range(21, 285, 10):
            pdf.line(x1=10, y1=y, x2=200, y2=y)

pdf.output('test.pdf')
