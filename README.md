# Dataverse

<img src="website/web_images/3d_glow.webp" height=50px align=right>

###### Data Visualisation Software & Personal Finance Tracker

<!--![Visitors](https://api.visitorbadge.io/api/visitors?path=multiverseweb/Dataverse%20&countColor=%2523263759&style=for-the-badge)-->

![Visitors](https://api.visitorbadge.io/api/visitors?path=multiverseweb2%2Dataverse%20&countColor=%23263759&style=flat&initial=5767)
![Github](https://img.shields.io/github/license/multiverseweb/Dataverse)
![Languages](https://img.shields.io/github/languages/count/multiverseweb/Dataverse?color=20B2AA)
![GitHub Repo stars](https://img.shields.io/github/stars/multiverseweb/Dataverse)
![GitHub contributors](https://img.shields.io/github/contributors/multiverseweb/Dataverse)
![GitHub issues](https://img.shields.io/github/issues/multiverseweb/Dataverse)
![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/multiverseweb/Dataverse)
![GitHub forks](https://img.shields.io/github/forks/multiverseweb/Dataverse)
![GitHub pull requests](https://img.shields.io/github/issues-pr/multiverseweb/Dataverse)
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/multiverseweb/Dataverse)
![GitHub last commit](https://img.shields.io/github/last-commit/multiverseweb/Dataverse)
![GitHub repo size](https://img.shields.io/github/repo-size/multiverseweb/Dataverse)
![GitHub total lines](https://sloc.xyz/github/multiverseweb/Dataverse)

### Featured In

<table>
<tr>
      <th>Event Logo</th>
      <th>Event Name</th>
    </tr>
    <tr>
        <td><img src="https://user-images.githubusercontent.com/63473496/213306279-338f7ce9-9a9f-4427-8c2a-3e344874498f.png#gh-dark-mode-only" width="200" height="auto" loading="lazy" alt="GSSoC Ext 24"/></td>
        <td><a href="https://gssoc.girlscript.tech/">GirlScript Summer of Code Ext (GSSoC'24) </a>2024</td>
    </tr>
   <tr>
        <td><img src="https://cdn.prod.website-files.com/63bc83b29094ec80844b6dd5/66fc35d92c74c4e4103f3673_Flyte-at-Hacktoberfest-2024.png" width="200" height="auto" loading="lazy" alt="Hacktoberfest 24"/></td>
        <td><a href="https://hacktoberfest.com/">Hacktober Fest</a> 2024</td>
    </tr>
</table>

---

### Table of Contents

| [About Dataverse](#what-does-this-software-do) | [Versions](#versions) | [Use Dataverse](#deployment-specifications) | [Repository Structure](#repository-structure) | [Preview](#preview) | [Software Representation](#software-representation) | [Make Contributions](#contributions) | [Website](#website) |
| :--------------------------------------------: | :-------------------: | :-----------------------------------------: | :-------------------------------------------: | :-----------------: | :-------------------------------------------------: | :----------------------------------: | :-----------------: |

---

### What does this software do?

- This software can be used to visualise data in many basic as well as advanced forms.
- It allows the user to download the generated charts.
- It can be used as a finance tracker, providing various useful outputs.
- It supports data inputs from excel sheets.
- The data can also be stored for later use.
- Uses encryption techniques to securely store your passwords.

---

### Versions

- 6550(24) `Latest`
- 06.02.24

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

- Open `software` folder in VSCode.

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
  CREATE DATABASE DATAVERSE;
  ```
  on your MySQL workbench or commandline client.

<highlight>For Website</highlight>

- You must have Node.js installed in your computer, if it is not, install it from [here](https://nodejs.org/en).
- After you have installed it, open the terminal, and run this command to install the required dependencies:
  ```
  npm install
  ```
- Then, install the Prettier extension (`Prettier - Code Formatter`) in order to format the code consistently accross all devices.

  <!-- <img src="./Documentation/images/prettier.PNG" width="600px"> -->

  ![Prettier extension image preview](documentation/images/prettier.png)

- After you have installed Prettier, press `Ctrl + Shift + p` to open the Command Palette and type `Reload window` and select the first option to reload, then prettier will be automatically applied.

---

### Repository Structure

📂 [Repository Structure](/Documentation/PROJECT_STRUCTURE.md)

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
![](/website/web_images/ER_diagram.png)

---

### Star History

<picture>
  <source
    media="(prefers-color-scheme: dark)"
    srcset="
      https://api.star-history.com/svg?repos=multiverseweb/Dataverse&type=Date&theme=dark
    "
  />
  
  <source
    media="(prefers-color-scheme: light)"
    srcset="
      https://api.star-history.com/svg?repos=multiverseweb/Dataverse&type=Date
    "
  />
  <img
    alt="Star History Chart"
    src="https://api.star-history.com/svg?repos=multiverseweb/Dataverse&type=Date&theme=dark"
  />
</picture>

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

### Stargazers ❤️

<div align='left'>

[![Stargazers repo roster for @multiverseweb/Dataverse](https://reporoster.com/stars/dark/multiverseweb/Dataverse)](https://github.com/multiverseweb/Dataverse/stargazers)

</div>

### Forkers ❤️

[![Forkers repo roster for @multiverseweb/Dataverse](https://reporoster.com/forks/dark/multiverseweb/Dataverse)](https://github.com/multiverseweb/Dataverse/network/members)

---

### Website

| <a href="https://multiverse-dataverse.netlify.app/"><img src="Documentation/images/netlify.svg"></a> | [Visit Dataverse's Website](https://multiverse-dataverse.netlify.app/) |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |

<sup><a href="#table-of-contents" align="right">Back to top</a></sup>

```

```
