import fpdf
import matplotlib
from matplotlib import pyplot as plt
from datetime import date

def save(u_name, total):
    # Validate that u_name and total are not empty or invalid
    if not u_name or not isinstance(total, (int, float)):
        print("Error: Invalid username or total value.")
        return

    #=================================================Designing and saving report PDF
    pdf = fpdf.FPDF()
    pdf.add_page()
    pdf.set_font("Times", size=12)
    pdf.set_fill_color(0, 0, 0)
    pdf.set_text_color(255, 255, 255)
    
    try:
        pdf.cell(200, 10, txt="Personal Finance Tracker & Data Visualization Software", ln=1, align="C", fill=True)
        pdf.cell(200, 10, txt="Date: {}".format(date.today()), ln=1, align="L", fill=True)
        pdf.cell(200, 10, txt="\n\nTotal={}".format(total), ln=1, align="L", fill=True)
        
        # Attempt to add the image; catch any file errors
        try:
            pdf.image('plot.png', x=None, y=None, w=190, h=120, type='', link='plot.png')
        except RuntimeError:
            print("Error: The image file 'plot.png' was not found. Please ensure it exists.")

        pdf.cell(200, 20, txt="-Tejas, Ojas & Nandana :)", ln=1, align="R", fill=True)

        # Save the PDF and handle any file writing errors
        pdf_file_name = "{}-{}.pdf".format(u_name.title(), date.today())
        pdf.output(pdf_file_name)
        print("File name: {}".format(pdf_file_name))

    except Exception as e:
        print("An error occurred while creating the PDF:", str(e))
