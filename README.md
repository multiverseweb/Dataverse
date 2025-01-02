# Dataverse
<img src="website/web_images/3d_glow.webp" height=50px align=right>

###### Data Visualisation Software & Finance Tracker

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

---

### Table of Contents

<table>
  <tr>
    <th><a href="#what-does-this-software-do">About Dataverse</a></th>
<th><a href="#preview">Application Preview</a></th>
    <th><a href="#versions">Versions</a></th>
    <th><a href="#repository-structure">Repository Structure</a></th>
    <th><a href="#deployment-specifications">Use Dataverse</a></th>
    <th><a href="#contributions">Make Contributions</a></th>
    <th><a href="#website">Website</a></th>
  </tr>
</table>

---

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

### What does this software do?
- Supports all data visualisation techniques, basic as well as advanced.
- Generates interactive, customizable and exportable graphs.
- Provides data storage for later use.
- Supports data inputs from excel sheets.
- Simplifies expense tracking and financial management.
- Allows user to download financial reports.
- Uses encryption techniques to securely store your passwords.
- View and manage data via a mobile-friendly website.
- Provides predictive analytics and trend analysis using ML techniques.

---

### Preview
<div align=center>

Software GUI
<br>
<img src="software/images/preview.png" width="800px">
<br><br>
<details> 
 <summary align=left><H4>View More</H4></summary><br>
Software Home Page
<br>
<img src="Documentation/images/home_UI.png" width="800px">
<br><br>
Visualised Data
<br>
<img src="website/web_images/finance_down.webp" width="800px">
<br><br>
Stored Data
<br>
<img src="website/web_images/finance_up.webp" width="800px">
</details>
</div>

---

### Versions

| Version | Description |
|-------------|-----------------|
| v.XM45.24 `Under Development` | High scale installable vesrion currently being developed, has improved UI based on glassmorphism. Makes the project mobile-friendly and provides more analytical features. Seeks major contributions through SWOC-S5. |
| v.6550.24 `Latest` | Current stable version that supports most of the data visualisation techniques and finance tracking. Major development done during GSSoC'24. |
| v.06.02.24 | Initial version developed on 6th February, 2024. Only supports finance tracking. |

---

### Repository Structure

| [**📂 View _Repository Structure_**](/Documentation/PROJECT_STRUCTURE.md) |
|-|

---

### Deployment Specifications
I. Navigate to the directory where you want to deploy the dataverse application and open terminal or command prompt there.

II. Run the following commands in terminal:

> ```
> git clone https://github.com/multiverseweb/Dataverse.git
> ```

III. Create a Virtual Environment (optional but recommended)
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

IV. Install dependencies:

> ```
> cd Dataverse
> ```
> ```
> pip install -r installation/requirements.txt  
> ```

V. Install MySQL if you don't have it already from [here](https://dev.mysql.com/downloads/installer/).

> [!IMPORTANT]
> Change the values of `DB_HOST`, `DB_USER` and `DB_PASSWORD` in [software/db_config.py](software/db_config.py) file according to your MySQL account.

VI. Run the application:

> ```
> python software/main.py
> ```

Now, the software should run smoothly with no errors, feel free to use the software and don't forget to give feedback on [Dataverse's website](https://multiverse-dataverse.netlify.app/)!

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

---

### Contributions

Want to make contributions to this project? ✨

| **[Read _contribution guidelines!_](Documentation/contributing.md)** |
|-|

---

### Our Valuable Contributors ❤️

[![Contributors](https://contrib.rocks/image?repo=multiverseweb/Dataverse)](https://github.com/multiverseweb/Dataverse/graphs/contributors)

### Stargazers ⭐

<div align='left'>

[![Stargazers repo roster for @multiverseweb/Dataverse](https://reporoster.com/stars/dark/multiverseweb/Dataverse)](https://github.com/multiverseweb/Dataverse/stargazers)

</div>

### Forkers 🍴

[![Forkers repo roster for @multiverseweb/Dataverse](https://reporoster.com/forks/dark/multiverseweb/Dataverse)](https://github.com/multiverseweb/Dataverse/network/members)

---
 
### Website
|<a href="https://multiverse-dataverse.netlify.app/"><img src="Documentation/images/netlify.svg"></a>|[Visit Dataverse's Website](https://multiverse-dataverse.netlify.app/)|
|-|-|

<sup><a href="#table-of-contents" align="right">Back to top</a></sup>

```

```
