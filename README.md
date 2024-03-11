# Personal Finance Tracker & Data Visualisation Software
>Project by [Nandana](https://github.com/nandanaap/), [Ojas](https://github.com/ojas-git/) & [Tejas](https://github.com/multiverseweb/)

>Technologies to be used:<br/>`#python #mysql`

>Python modules:<br/>`#mysql.connector #numpy #pandas #matplotlib #time #datetime #getpass #math #fpdf/#reportlab`

>User-defined modules:<br/>`#functions #plot`

---
##### :octocat:&nbsp;&nbsp;26-02-2024
---

>## Abstract
>- In this project, we will be allowing the users to track their money by creating an account on our software.
>- Their data will be stored in `MySQL` database which can be fetched using the unique ID generated during account creation.
>- We can visualise the data in various ways as requested by the user using `matplotlib`.
>- Paydays or EMI/rent payment days can be plot on the graph using a vertical line.
>- Data wrangling can be performed (if required) using `pandas` module of `python`.
>- Some useful mathematical operations can also be performed on the data (like calculating Total money, profit, loss, interest, etc.).
>- The users will also be able to download the report generated. This can be done using puthon module `fpdf` or `reportlab`.
```python
NOTE:
- If the user just wants to visualise any form of data without saving it, he/she can continue as guest.
- Guests will also be able to download the graphs.
```

---
##### :octocat:&nbsp;&nbsp;27-02-2024
---
>## How to set up code in your computer?
>1. Save/copy the files [main.py](https://github.com/multiverseweb/finance_tracker/blob/main/main.py), [functions.py](https://github.com/multiverseweb/finance_tracker/blob/main/functions.py) and [plot.py](https://github.com/multiverseweb/finance_tracker/blob/main/plot.py) on your computer.
>2. In the `connecting mySQL` section of `main.py`, `functions.py` and `plot.py` files, write the host, user and passwd associated with your MySQL.
>3. Open MySQL commandline client and execute the following query:
   ```mysql
   create database finance;
   ```
>4. Now, run the python program.


>★ NOTE:
>You can pip install the python modules if you don't have them already on your computer use this command in command prompt:

```
python -m pip install {moduleName}
```

---
##### :octocat:&nbsp;&nbsp;28-02-2024
---
>## How to contribute?

>| Nandana | Ojas | Tejas |
>|:----------:|:---:|:---:|
>| Basic mathematical operations | Loan operations | Guest operations|
>| Dowloading report option | User operations | User account details |
>| | | Output theme & structure |

>- As you have access to this repository, you can make changes to any file.
>- Add code/files with proper comments.
>- Keep appending to this readme file `date-wise`. :octocat:

---
##### :octocat:&nbsp;&nbsp;02-03-2024
---
- Fixed 'Add Details' option under user operations.
- Increased the y-axis variables limit. (16)

---
#### :octocat:&nbsp;&nbsp;06-03-2024
---
- **Basic** code for report downloading function is added in the file [save_report.py](save_report.py).
- Output report can be seen in [Tejas-2024-03-06.pdf](Tejas-2024-03-06.pdf).
  
---
#### :octocat:&nbsp;&nbsp;07-03-2024
---
- Added option for plotting data in finance tracker. Code is in file [plot.py](plot.py).
- Performed data wrangling for dealing with the dates on which data wasn't updated by user.
  
  `Happy coding :)`
  
  ---
