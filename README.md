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

### Project Mentors
[Jency Maheshwari](https://github.com/jency1)

[Shubhrangi Pathak](https://github.com/shubhrangipathak)

#### Read the description below and [start contributing](#contributions) now! If you like the project, show some love ❤️ and star the repo! ⭐


---

# Dataverse
<img src="website/web_images/2dglow.png" height=50px align=right>

###### Data Visualisation Software & Personal Finance Tracker

---

![Github](https://img.shields.io/github/license/multiverseweb/Dataverse?style=for-the-badge)
![Visitors](https://api.visitorbadge.io/api/visitors?path=multiverseweb/Dataverse%20&countColor=%2523263759&style=for-the-badge)
![GitHub Repo stars](https://img.shields.io/github/stars/multiverseweb/Dataverse?style=for-the-badge)
![GitHub contributors](https://img.shields.io/github/contributors/multiverseweb/Dataverse?style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues/multiverseweb/Dataverse?style=for-the-badge)
![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/multiverseweb/Dataverse?style=for-the-badge)
![GitHub pull requests](https://img.shields.io/github/issues-pr/multiverseweb/Dataverse?style=for-the-badge)
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/multiverseweb/Dataverse?style=for-the-badge)
![GitHub forks](https://img.shields.io/github/forks/multiverseweb/Dataverse?style=for-the-badge)
![GitHub last commit](https://img.shields.io/github/last-commit/multiverseweb/Dataverse?style=for-the-badge)
![GitHub repo size](https://img.shields.io/github/repo-size/multiverseweb/Dataverse?style=for-the-badge)

### Featured In

| Event Logo | Event Name | Event Description |
|------------|------------|-------------------|
| <img src="https://user-images.githubusercontent.com/63473496/213306279-338f7ce9-9a9f-4427-8c2a-3e344874498f.png#gh-dark-mode-only" width="400" height="auto"> | **GirlScript Summer of Code Extended 2024** | [GirlScript Summer of Code](https://gssoc.girlscript.tech/) is a three-month-long Open Source Program conducted every summer by GirlScript Foundation. It is an initiative to bring more beginners to Open-Source Software Development. |

---

### Table of Contents

| [About Dataverse](#what-does-this-software-do) | [Use Dataverse](#deployment-specifications) | [Preview](#preview) | [Software Representation](#software-representation) | [Make Contributions](#contributions) | [Website](#website) |
|:--:|:--:|:--:|:--:|:--:|:--:|

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
<img src="software/images/preview.png" width="800px">
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
### Contributions
<sup><a href="#table-of-contents" align="right">Back to top</a></sup>

Want to contribute to this project? Follow these steps:

- Star the Repository.
- Go to [issues](https://github.com/multiverseweb/Dataverse/issues), find an issue that you can solve or create a new issue.
- Fork the repository.
- Create a new branch (`git checkout -b feature-branch`).
- Go to [`line no. 1` in script.js](https://github.com/multiverseweb/Dataverse/blob/main/website/script.js#L1-L2) and append the name of your city to the `cities` array. (optional)
- Make your contributions and commit them (`git commit -m 'Add feature'`).
- Push to the branch (`git push origin feature-branch`).
- Create a Pull Request, so I can review and merge it.




### Our Valuable Contributors ❤️✨

[![Contributors](https://contrib.rocks/image?repo=multiverseweb/Dataverse)](https://github.com/multiverseweb/Dataverse/graphs/contributors)
 
---
### Website

Deployed on

<img height="50px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/Netlify_logo_%282%29.svg/1200px-Netlify_logo_%282%29.svg.png">

You can visit the live site for Dataverse and related tools [here](https://multiverse-dataverse.netlify.app/).


<sup><a href="#table-of-contents" align="right">Back to top</a></sup>

