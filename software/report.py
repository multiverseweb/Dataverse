import fpdf
import matplotlib
from matplotlib import pyplot as plt
from datetime import datetime, timedelta,date

def save(u_name,total):
    #=================================================Designing and saving report PDF
    pdf = fpdf.FPDF()
    pdf.add_page()
    pdf.set_font("Times", size=12)
    pdf.set_fill_color(0, 0, 0)
    pdf.set_text_color(255,255,255)
    #pdf.cell(200, 40,'Colored cell', 0, 1, 'C',)
    pdf.cell(200, 10, txt="Personal Finance Tracker & Data Visualization Software", ln=1, align="C", fill=True)
    pdf.cell(200, 10, txt="Date: {}".format(date.today()), ln=1, align="L", fill=True)
    pdf.cell(200, 10, txt="\n\nTotal={}".format(total), ln=1, align="L", fill=True)
    pdf.image('plot.png', x = None, y = None, w = 190, h = 120, type = '', link = 'plot.png')
    pdf.cell(200, 20, txt="-Tejas, Ojas & Nandana :)", ln=1, align="R", fill=True)
    pdf.output("{}-{}.pdf".format(u_name.title(),date.today()))
    print("File name: {}-{}.pdf".format(u_name.title(),date.today()))
