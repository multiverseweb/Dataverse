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
    if (!button || !indicator) return;

    // Adjust the indicator position to align with the selected button
    const adjustment = (button.offsetHeight - indicator.offsetHeight) / 2;
    indicator.style.top = `${button.offsetTop + adjustment}px`;

    // Update the indicator's color based on the theme
    const currentTheme = localStorage.getItem('theme');
    if (currentTheme === 'light') {
        indicator.style.backgroundImage = "radial-gradient(circle, rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0) 70%)"; // Black glow in light mode
    } else {
        indicator.style.backgroundImage = "radial-gradient(circle, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0) 70%)"; // White glow in dark mode
    }

    console.log(`Indicator updated: ${currentTheme} mode, positioned at ${button.id}`);
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

function systemDefault() {
    const theme = localStorage.getItem('theme');
    const defaultButton = document.getElementById("defaultButton");

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
    console.log("Light button clicked");
    light(false);
});
document.getElementById("darkButton").addEventListener("click", () => {
    console.log("Dark button clicked");
    dark(false);
});
document.getElementById("defaultButton").addEventListener("click", () => {
    console.log("Default button clicked");
    systemDefault();
    updateIndicator(document.getElementById("defaultButton"));
});
