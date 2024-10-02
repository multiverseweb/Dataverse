# GSSoc'24  <a href="https://codeittool.netlify.app">Extended<img src="https://user-images.githubusercontent.com/63473496/153487849-4f094c16-d21c-463e-9971-98a8af7ba372.png" height=40px align=right></a>

## Tech Stack

![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![MySQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white) 
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%2311557c.svg?style=for-the-badge&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-blue?style=for-the-badge&logo=python&logoColor=white) 
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) 
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E) 
![Microsoft Excel](https://img.shields.io/badge/Microsoft_Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)

#### Read the description below and [start contributing](#contributions) now! If you like the project, show some love ❤️ and star the repo! ⭐
---

# Dataverse
<img src="website/web_images/2dglow.png" height=50px align=right>

###### Data Visualisation Software & Personal Finance Tracker

---

[![License: MIT](https://cdn.prod.website-files.com/5e0f1144930a8bc8aace526c/65dd9eb5aaca434fac4f1c34_License-MIT-blue.svg)](/LICENSE#L3)
![GitHub Issues](https://img.shields.io/github/issues/multiverseweb/Dataverse)
![GitHub Pull Requests](https://img.shields.io/github/issues-pr/multiverseweb/Dataverse)
![Stars](https://img.shields.io/github/stars/multiverseweb/Dataverse)

### Table of Contents

| [About Dataverse](#what-does-this-software-do) | [Use Dataverse](#deployment-specifications) | [Preview](#preview) | [Software Representation](#software-representation) | [Technologies Used](#technologies-used) | [Make Contributions](#contributions) | [Website](#website) |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|

---

### What does this software do?
- This software can be used to visualise data in many basic as well as advanced forms.
- It allows the user to download the generated charts.
- It can be used as a finance tracker, providing various useful outputs.
- It supports data inputs from excel sheets.
- The data can also be stored for later use.
- Uses encryption techniques to securely store your passwords.

---

### Deployment Specifications

Dataverse is currently under development. It will be available for installastion soon.

However, you can follow these steps to run the project locally on your computer:
> [!IMPORTANT]
> Don't forget to read the [prerequisites](#prerequisites).


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
<img src="website/web_images/about_down.png" width="800px">
<br><br>
<details> 
 <summary align=left><H4>View More</H4></summary><br>
Visualised Finance Data
<br>
<img src="website/web_images/preview.png" width="800px">
<br><br>
Relational Data
<br>
<img src="website/web_images/data.png" width="800px">
</details>
</div>

---

### Software Representation
<sup><a href="#table-of-contents" align="right">Back to top</a></sup>

ER Diagram for Finance Tracker
![](website/web_images/ER_diagram.png)

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
![Microsoft Excel](https://img.shields.io/badge/Microsoft_Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)

---
### Contributions
<sup><a href="#table-of-contents" align="right">Back to top</a></sup>

Want to show yourself on the contributions-map?

- Contribute to this project.

> [!IMPORTANT]
> Create a new branch `gssoc-yourName` before sending the Pull Request.
- Go to [issues](https://github.com/multiverseweb/Dataverse/issues), resolve the one that you can or create a new issue.
- Go to [`line no. 1` in script.js](https://github.com/multiverseweb/Dataverse/blob/main/website/script.js#L1-L2).
- Append the name of your city to the `cities` array.
- Create a `pull-request` so I can review and merge it.

---
### Website

Deployed on

<img height="50px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/Netlify_logo_%282%29.svg/1200px-Netlify_logo_%282%29.svg.png">

You can visit the live site for Dataverse and related tools [here](https://multiverse-dataverse.netlify.app/).


<sup><a href="#table-of-contents" align="right">Back to top</a></sup>

<h1>Our Valuable Contributors ❤️✨</h1>

[![Contributors](https://contrib.rocks/image?repo=multiverseweb/Dataverse)](https://github.com/multiverseweb/Dataverse/graphs/contributors)
 
