// Selecting elements
var l1 = document.getElementById("l1");
var l2 = document.getElementById("l2");
var l3 = document.getElementById("l3");
var burger = document.getElementById("burger");
var lines = document.getElementById("lines");
var cross = document.getElementById("cross");
var plane = document.getElementById("plane");
var body = document.getElementById("body");
var buttons = document.getElementById("buttons");
var indicator = document.getElementById("indicator");
var codeOfConductSection = document.getElementById("codeOfconduct");

// Adding error checking for missing elements
if (!indicator) {
    console.error("Indicator element is missing");
}

function show() {
    l2.style.opacity = 0;
    l1.style.transform = "rotate(-45deg)";
    l3.style.transform = "rotate(45deg)";
    burger.style.display = "none";
    cross.style.display = "block";
    plane.style.right = 0;
    body.style.overflowY = "hidden";
    buttons.style.marginLeft = 0;
}

function hide() {
    l2.style.opacity = 1;
    l1.style.transform = "rotate(0deg)";
    l3.style.transform = "rotate(0deg)";
    burger.style.display = "block";
    cross.style.display = "none";
    plane.style.right = "-100vw";
    body.style.overflowY = "scroll";
    buttons.style.marginLeft = "-60px";
}

function updateIndicator(button) {
    // Calculate the vertical adjustment for perfect centering of the indicator over the button
    const adjustment = (button.offsetHeight - indicator.offsetHeight) / 2;

    // Correct the top position based on the button's offsetTop value
    indicator.style.top = `${button.offsetTop + adjustment}px`;

    // Apply the correct glow effect based on the current theme
    const currentTheme = localStorage.getItem('theme');
    if (currentTheme === 'light') {
        indicator.style.backgroundImage = "radial-gradient(circle, rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0) 70%)"; // Black glow in light mode
        indicator.style.boxShadow = "none"; // No box-shadow needed for glow
    } else {
        indicator.style.backgroundImage = "radial-gradient(circle, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0) 70%)"; // White glow in dark mode
        indicator.style.boxShadow = "none"; // No box-shadow needed for glow
    }
}



function light(flag) {
    localStorage.setItem('theme', 'light');
    body.style.backgroundColor = "white";
    body.style.color = "black";

    // If the codeOfConductSection is present, change its color
    if (codeOfConductSection) {
        codeOfConductSection.style.backgroundColor = "white";
        codeOfConductSection.style.color = "black";
    }

    const lightButton = document.getElementById("lightButton");
    updateIndicator(lightButton);
}

function dark(flag) {
    localStorage.setItem('theme', 'dark');
    body.style.backgroundColor = "black";
    body.style.color = "white";

    if (codeOfConductSection) {
        codeOfConductSection.style.backgroundColor = "black";
        codeOfConductSection.style.color = "white";
    }

    const darkButton = document.getElementById("darkButton");
    updateIndicator(darkButton);
}

// Display the current year in the copyright section
function displayCopyright() {
    const year = new Date().getFullYear();
    document.getElementById("copyright").innerText = year;
  }

function systemDefault() {
    const theme = localStorage.getItem('theme');
    const defaultButton = document.getElementById("defaultButton");
    displayCopyright();
    if (theme === 'light') {
        light(true);
        updateIndicator(document.getElementById("lightButton"));
    } else if (theme === 'dark') {
        dark(true);
        updateIndicator(document.getElementById("darkButton"));
    } else {
        if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
            dark(true);
            updateIndicator(document.getElementById("darkButton"));
        } else {
            light(true);
            updateIndicator(document.getElementById("lightButton"));
        }
    }
}

// Initialize the theme and indicator position on page load
document.addEventListener("DOMContentLoaded", systemDefault);

// Add event listeners to ensure the glow moves when buttons are clicked
document.getElementById("lightButton").addEventListener("click", () => {
    light(false);
});
document.getElementById("darkButton").addEventListener("click", () => {
    dark(false);
});
document.getElementById("defaultButton").addEventListener("click", () => {
    systemDefault();
    updateIndicator(document.getElementById("defaultButton"));
});
