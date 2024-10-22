import fpdf
import matplotlib
from matplotlib import pyplot as plt
from datetime import date
import os

def save(u_name, total):
    # Validate that u_name and total are not empty or invalid
    if not u_name or not isinstance(u_name, str):
        print("Error: Invalid username. Please provide a valid string.")
        return
    
    if not isinstance(total, (int, float)):
        print("Error: Invalid total value. Please provide a numeric value.")
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
        image_path = 'plot.png'
        if not os.path.exists(image_path):
            print("Error: The image file 'plot.png' was not found. Please ensure it exists.")
        else:
            try:
                pdf.image(image_path, x=None, y=None, w=190, h=120, type='', link=image_path)
            except RuntimeError as e:
                print("Error while adding image to PDF:", str(e))

        pdf.cell(200, 20, txt="-Tejas, Ojas & Nandana :)", ln=1, align="R", fill=True)

        # Save the PDF and handle any file writing errors
        pdf_file_name = "{}-{}.pdf".format(u_name.title(), date.today())
        pdf.output(pdf_file_name)
        print("File name: {}".format(pdf_file_name))

    except Exception as e:
        print("An error occurred while creating the PDF:", str(e))
