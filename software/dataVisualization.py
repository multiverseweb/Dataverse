from tkinter import messagebox  # for showing messages
from tkinter import *
from matplotlib.gridspec import GridSpec  # for showing graph grid
from functools import partial  # for calling button functions
import matplotlib.pyplot as plt  # for plotting graphs
import numpy as np  # for x-axis time arange
import report  # for report pdf
import mysql.connector as my  # connecting mysql

#===============================================================================================================plot colors
colors = ["#fde725", "#5ec962", "#21918c", "#3b528b", "#440154", "#f89540", "#cc4778", "cyan", "#7e03a8", "tomato",
          "tan", "#0d0887", "green", "blue", "indigo", "violet"]

#===============================================================================================================connecting mySQL
mycon = my.connect(host='localhost', user='root', passwd='tejas123', database='finance')
cursor = mycon.cursor()


def plot_data(heading, x, y, dependent, c):
    """Helper function to plot the data."""
    fig, ax = plt.subplots()
    width = 1

    for i in range(dependent):
        if c == 1:
            plt.bar(x, y[i + 1], label=y[0][i], color=colors[i], linewidth=0.7, width=width)
        elif c == 2:
            plt.hist(x, y[i + 1], label=y[0][i], color=colors[i], linewidth=0.7, width=width)
        elif c == 3:
            plt.scatter(x, y[i + 1], label=y[0][i], color=colors[i], linewidth=0.7)
        else:
            plt.plot(x, y[i + 1], label=y[0][i], color=colors[i], linewidth=0.7)
        width -= 0.2

    plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0)
    plt.title(heading)
    plt.xticks(rotation=30)
    plt.xlabel("Independent Variable")
    ax.spines['bottom'].set_color('teal')
    ax.spines['top'].set_color('#ffffff40')
    ax.spines['right'].set_color('#ffffff40')
    ax.spines['left'].set_color('darkturquoise')
    ax.grid(linestyle="dashed", linewidth=1, alpha=0.25)
    plt.show()


def line(c):
    import mainGUI
    form = Frame(mainGUI.root, bg="#171717", relief=SUNKEN)
    form.pack(side=TOP, fill=Y, pady=140, padx=(0, 200))

    title_var = StringVar()
    x_var = StringVar()
    y_var = IntVar()
    
    title_label = Label(form, text='Title: ', font=('calibre', 10))
    title_entry = Entry(form, textvariable=title_var, font=('calibre', 10))
    x_label = Label(form, text='Name of independent variable: ', font=('calibre', 10))
    x_entry = Entry(form, textvariable=x_var, font=('calibre', 10))
    y_label = Label(form, text='No. of dependent variables: ', font=('calibre', 10))
    y_entry = Entry(form, textvariable=y_var, font=('calibre', 10))
    title_label.grid(row=0, column=0)
    title_entry.grid(row=0, column=1)
    x_label.grid(row=1, column=0)
    x_entry.grid(row=1, column=1)
    y_label.grid(row=2, column=0)
    y_entry.grid(row=2, column=1)
    sub_btn = Button(form, text="Create", width=15, cursor="hand2")
    sub_btn.grid(row=3, column=1)

    form.mainloop()

    heading = title_var.get()
    x_label = x_var.get()
    start = int(input("{} start value: ".format(x_label)))
    end = int(input("{} end value: ".format(x_label)))
    width = int(input("{} class width: ".format(x_label)))

    # Use local count variable instead of global
    count = 0
    x = []
    for i in range(start, end + 1, width):
        x.append(i)
        count += 1

    d_attr = []
    while True:
        dependent = int(input("No. of dependent attributes: "))
        if dependent > 16:
            print("Too many variables! The maximum limit is 16\nNOTE: Enter 0 to exit.")
        elif dependent == 0:
            break
        else:
            break

    if dependent != 0:
        for i in range(dependent):
            d_attr.append(input("Dependent Attribute {}: ".format(i + 1)))
        
        y = [d_attr]  # Initialize y with dependent attributes
        
        for i in range(dependent):
            print("Enter {} observations of {}: ".format(count, d_attr[i]))
            values = []
            for j in range(count):
                value = float(input("{}{}: ".format(d_attr[i], j + 1)))
                values.append(value)
            y.append(values)
        
        # Call the helper function to plot data
        plot_data(heading, x, y, dependent, c)

    # Close MySQL connection after data fetching
    mycon.close()
