# Dataverse
<img src="web_images/2dglow.png" height=50px align=right>

###### Data Visualisation Software & Personal Finance Tracker

---
### Table of Contents

| [About Dataverse](#what-does-this-software-do) | [Use Dataverse](#use-dataverse) | [Preview](#preview) | [Software Representation](#software-representation) | [Technologies Used](#technologies-used) | [Make Contributions](#contributions) | [Website](#website) |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|

---

### What does this software do?
- This software can be used to visualise data in many forms.
- It allows the user to download the generated charts.
- It can be used as a finance tracker, providing various useful outputs.
- The data can also be stored for later use.

---

### Use Dataverse

Dataverse is currently under development. It will be available for installastion soon.

* Steps to run the project locally:
  
   | Don't forget to read the [prerequisites](#prerequisites). |
   |--|

   - Clone the project
   
      ```
     git clone https://github.com/multiverseweb/Dataverse.git
      ```

   -  Open `software` folder in VSCode.

      ```
      cd Dataverse/software
      ```

   - Go to `mainGUI.py` and run it.

Now the software should run locally with no errors, feel free to use the software and don't forget to give feedback on the [website](https://multiverse-dataverse.netlify.app/)!

---

### Prerequisites
<highlight>For Data Visualization</highlight>
- You must have a python interpreter installed on your computer.
- You must have python packages such as `numpy, pandas, matplotlib, tkinter`.

  ```
  pip install package_name
  ```
<highlight>For Finance Tracker</highlight>
- For using the Finance Tracker, you must have `MySQL` installed on your computer. If you don't have it you can download it from [here](https://dev.mysql.com/downloads/installer/).
- Go to `line no. 15` under `connecting MySQL` section of `financeTracker.py` and change the values of `host, user and passwd` according to your MySQL account.
- Also, run the command
  ```
  CREATE DATABASE FINANCE;
  ```
  on your MySQL workbench or commandline client.

---

### Preview
<sup><a href="#table-of-contents" align="right">Back to top</a></sup>
<div align=center>

Software GUI
<br>
<img src="web_images/about_down.png" width="800px">
<br><br>
<details> 
 <summary align=left><H4>View More</H4></summary><br>
Visualised Finance Data
<br>
<img src="preview.png" width="800px">
<br><br>
Relational Data
<br>
<img src="data.png" width="800px">
</details>
</div>

---

### Software Representation
<sup><a href="#table-of-contents" align="right">Back to top</a></sup>

ER Diagram for Finance Tracker
![](ER_diagram.png)

---

### Technologies used
<sup><a href="#table-of-contents" align="right">Back to top</a></sup>

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![MySQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white) 
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%2311557c.svg?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-blue?style=for-the-badge&logo=python&logoColor=white) 
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) 
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E) 

---
### Contributions
<sup><a href="#table-of-contents" align="right">Back to top</a></sup>

Want to show yourself on the contributions-map?

- Contribute to this project.
- Go to `line no. 1` in [script.js](script.js).
- Append the name of your city to the `cities` array.
- Create a `pull-request` so I can review and merge it.

---
### Website
<sup><a href="#table-of-contents" align="right">Back to top</a></sup>

Deployed on

<img height="50px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/Netlify_logo_%282%29.svg/1200px-Netlify_logo_%282%29.svg.png">

You can visit the live site for Dataverse and related tools [here](https://multiverse-dataverse.netlify.app/).
