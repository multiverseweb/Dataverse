import fpdf
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
from datetime import datetime, timedelta,date

t = np.arange(datetime(2023,2,15), datetime(2024,12,25), timedelta(days=10)).astype(datetime)
#style.use("ggplot")
plt.style.use('dark_background')
#======================================================================================================================================================
cash = [1,3,3,3,3,3,5.5,8,7,7,6.25,6.1,6.5,6.6,6.5,6.5,6.5,6.5,6.5,6.5,6.5,6.6,6.5,6.5,6.5,6.5,6.5,6.5,9,9.56,9.56,9.56,10.56,12.06,11.56,11.56,11.56,11.00]
gold = [5.7,5.7,5.9,6.1,6.3,6.2,6.2,6.3,6.3,6.5,6,6,6,6,6,6,6,6,6,6,6,6,6.1,6,6,6,6,6,10,9.7,9.54,9.758,9.6435,9.655,9.649,9.7095,9.4897,9.7957]
commo=[1.682,2.97,2.97,3.47,3.47,3.47,3.47]
stock=[0,0,0,0,0,0,0]
targets=[]
#=====================================================================================================================================================
sumcc=[]
stocks=[]
for i in range(31):
    stocks.append(0)
stocks.extend(stock)
for i in range(68-len(stocks)):
    stocks.append(stocks[-1])

for i in range(68-len(cash)):
    cash.append(cash[-1])
    gold.append(gold[-1])
#===================================Adding Commodity
sumcgcs=[]
commodity=[]
for i in range(31):
    commodity.append(0)
commodity.extend(commo)
for i in range(68-len(commodity)):
    commodity.append(commodity[-1])
#====================================================
for i in range(31):
    targets.append(None)
targets.append(21)
for i in range(68-len(targets)-1):
    targets.append(None)
targets.append(100)

last=[datetime(2024,12,25)]

for i in range(len(cash)):
    sumcc.append(cash[i]+commodity[i])
for i in range(68-len(sumcc)):
    sumcc.append(None)

for i in range(len(cash)):
    sumcgcs.append(cash[i]+gold[i]+commodity[i]+stocks[i])
#print("Total= INR","{:,}".format(sumcgcs[-1]*1000))
for i in range(68-len(sumcgcs)):
    sumcgcs.append(None)

fig, ax=plt.subplots()
plt.plot(t,sumcgcs, label="Total",color="yellow",linewidth=0.7)
plt.plot(t,sumcc, label="In hand",color="cyan",linewidth=0.7)
plt.plot(t,cash, label="Fiat",color="tomato",linewidth=0.7)
plt.plot(t,gold, label="Gold",color="gold",linewidth=0.7)
plt.plot(t,commodity, label="Commodity",color="springgreen",linewidth=0.7)
plt.plot(t,stocks, label="Stocks",color="b",linewidth=0.7)
plt.legend(loc="upper left")
plt.title("For Year 2023 & 2024")
plt.xlabel("Time")
plt.ylabel("Amount (₹1000 * y)")
plt.xticks(rotation=30)
plt.xlim(datetime(2023,1,15), datetime(2024,12,25))
ax.xaxis.set_major_locator(matplotlib.dates.MonthLocator(interval=1)) 
plt.ylim(0,101)
plt.locator_params(axis='y', nbins=21) 
plt.axvline(x = date.today(), color = 'lime',linewidth = 0.5,linestyle = "dashed",label="Today")
plt.scatter(t,targets, label="Target",color='yellow',marker='*')
ax.spines['bottom'].set_color('teal')
ax.spines['top'].set_color('#ffffff40') 
ax.spines['right'].set_color('#ffffff40')
ax.spines['left'].set_color('darkturquoise')
ax.grid(linestyle = "dashed",linewidth = 1, alpha = 0.25)
plt.rcParams['figure.figsize'] = [15,10]
#=================================================Saving graph image to insert in report pdf
plt.savefig("example.png", dpi=300)
#plt.show()

#=================================================Designing and saving report PDF
pdf = fpdf.FPDF()
pdf.add_page()
pdf.set_font("Times", size=12)
pdf.set_fill_color(0, 0, 0)
pdf.set_text_color(255,255,255)
#pdf.cell(200, 40,'Colored cell', 0, 1, 'C',)
pdf.cell(200, 10, txt="Personal Finance Tracker & Data Visualization Software", ln=1, align="C", fill=True)
pdf.image('example.png', x = None, y = None, w = 190, h = 120, type = '', link = 'example.png')
pdf.cell(200, 20, txt="-Tejas, Ojas & Nandana :)", ln=1, align="R", fill=True)
pdf.output("Tejas-{}.pdf".format(date.today()))
print("Report Downloaded Successfully. ✓")
