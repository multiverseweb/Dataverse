# Dataverse
<img src="website/web_images/3d_glow.webp" height=50px align=right>

###### Data Visualisation Software & Personal Finance Tracker

<!--![Visitors](https://api.visitorbadge.io/api/visitors?path=multiverseweb/Dataverse%20&countColor=%2523263759&style=for-the-badge)-->


![Visitors](https://api.visitorbadge.io/api/visitors?path=multiverseweb2%2Dataverse%20&countColor=%23263759&style=flat&initial=5767)
  ![License](https://img.shields.io/badge/License-CC%20BY--NC--ND%204.0-4e3eb5)
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
  <a href="https://multiverse-dataverse.netlify.app/"><img alt="Website" src="https://img.shields.io/website?url=https%3A%2F%2Fmultiverse-dataverse.netlify.app%2F&up_message=awake&up_color=%2300d18f&down_message=asleep&down_color=red&style=flat">
</a>

  
### Featured In

<table>
<tr>
      <th>Event Logo</th>
      <th>Event Name</th>
    </tr>
<tr>
        <td><img src="Documentation/images/SWOC.jpg" width="200" height="auto" loading="lazy" alt="SWOC"/></td>
        <td><a href="https://www.socialwinterofcode.com/">Social Winter of Code Season-5 (SWOC) </a>2024-2025</td>
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

<table>
  <tr>
    <th><a href="#what-does-this-software-do">About Dataverse</a></th>
    <th><a href="#versions">Versions</a></th>
    <th><a href="#deployment-specifications">Use Dataverse</a></th>
    <th><a href="#repository-structure">Repository Structure</a></th>
    <th><a href="#preview">Preview</a></th>
    <th><a href="#software-representation">Software Representation</a></th>
    <th><a href="#contributions">Make Contributions</a></th>
    <th><a href="#website">Website</a></th>
  </tr>
</table>

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

- v.XM45'24 Under Development
- v.6550(24) Latest
- v.06.02.24

---

### Prerequisites
<highlight>For Data Visualization</highlight>
- Ensure that a Python interpreter is installed on your computer. If not, download it from [ Python's official website](https://www.python.org/downloads/).

<highlight>For Finance Tracker</highlight>
- Install MySQL on your computer. If you don't have it, you can download it from [here](https://dev.mysql.com/downloads/installer/).

---

### Development Specifications

1. **Clone the Project**  
    ``` 
    git clone https://github.com/multiverseweb/Dataverse.git
    ```

2. **Create a Virtual Environment (optional but recommended)**
  - On Windows:

    ```
    python -m venv venv
    venv\Scripts\activate
    ```

  - On macOS/Linux:

    ```
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Navigate to the Project's software Directory**  
   
    ```
    cd Dataverse/software
    ```

4. **Install Dependencies**

  -  Install all the required Python packages using `requirements.txt`:

      ```
      pip install -r ../installation/requirements.txt
      ```

5. **Finance Tracker Setup**

- Open `financeTracker.py` (located in Dataverse/software/) and update `line no. 17` under the `connecting MySQL` section with your MySQL credentials (`host, user, and passwd`).
- Also, run the command
  ```
  CREATE DATABASE DATAVERSE;
  ```
  on your MySQL workbench or commandline client.

6. **Run the Project**

  - Run main.py using the command:

    ```
    python main.py
    ```  

  - Alternatively, open `main.py` in VSCode and run it.

7. **Deactivate the Virtual Environment**

- After you’re done working with the project, you can deactivate the virtual environment:

  ```
  deactivate
  ```

Now the software should run locally with no errors, feel free to use the software and don't forget to give feedback on the [website](https://multiverse-dataverse.netlify.app/)!

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
<img src="website/web_images/finance_down.webp" width="800px">
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
- Create a new branch (git checkout -b feature-branch).
- Go to [line no. 1 in script.js](https://github.com/multiverseweb/Dataverse/blob/main/website/scripts/script.js#L5-L7) and append the name of your city to the cities array. (optional)
- Make your contributions and commit them (git commit -m 'Add feature').
- Push to the branch (git push origin feature-branch).
- Create a Pull Request, so I can review and merge it.




### Our Valuable Contributors ❤✨

[![Contributors](https://contrib.rocks/image?repo=multiverseweb/Dataverse)](https://github.com/multiverseweb/Dataverse/graphs/contributors)


### Stargazers ❤

<div align='left'>

[![Stargazers repo roster for @multiverseweb/Dataverse](https://reporoster.com/stars/dark/multiverseweb/Dataverse)](https://github.com/multiverseweb/Dataverse/stargazers)


</div>

### Forkers ❤

[![Forkers repo roster for @multiverseweb/Dataverse](https://reporoster.com/forks/dark/multiverseweb/Dataverse)](https://github.com/multiverseweb/Dataverse/network/members)

---
 
### Website
|<a href="https://multiverse-dataverse.netlify.app/"><img src="Documentation/images/netlify.svg"></a>|[Visit Dataverse's Website](https://multiverse-dataverse.netlify.app/)|
|-|-|


<sup><a href="#table-of-contents" align="right">Back to top</a></sup>