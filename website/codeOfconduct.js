var l1 = document.getElementById("l1");
var l2 = document.getElementById("l2");
var l3 = document.getElementById("l3");
var burger = document.getElementById("burger");
var lines = document.getElementById("lines");
var cross = document.getElementById("cross");
var plane = document.getElementById("plane");
var body = document.getElementById("body");
var buttons = document.getElementById("buttons");
var shadow = document.getElementById("shadow");
var codeOfConductSection = document.getElementById("codeOfconduct");
const navbar = document.querySelector('navbar');

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
  // Set the position of the indicator to align with the selected button
  const adjustment = (button.offsetHeight - indicator.offsetHeight) / 2;
  indicator.style.top = `${button.offsetTop + adjustment}px`;

  // Set the color of the indicator based on the theme
  const currentTheme = localStorage.getItem('theme');
  if (currentTheme === 'light') {
    indicator.style.backgroundImage = "radial-gradient(circle, rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0) 70%)"; // Black glow in light mode
  } else {
    indicator.style.backgroundImage = "radial-gradient(circle, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0) 70%)"; // White glow in dark mode
  }
}

function light(flag) {
  localStorage.setItem('theme', 'light');
  body.style.backgroundColor = "white";
  body.style.color = "black";

  codeOfConductSection.style.backgroundColor = "white";
  codeOfConductSection.style.color = "black";

  const lightButton = document.getElementById("lightButton");
  updateIndicator(lightButton);
}

function dark(flag) {
  localStorage.setItem('theme', 'dark');
  body.style.backgroundColor = "black";
  body.style.color = "white";

  codeOfConductSection.style.backgroundColor = "black";
  codeOfConductSection.style.color = "white";

  const darkButton = document.getElementById("darkButton");
  updateIndicator(darkButton);
}

function systemDefault() {
  const theme = localStorage.getItem('theme');
  const defaultButton = document.getElementById("defaultButton");

  if (theme === 'light') {
    light(true);
    updateIndicator(document.getElementById("lightButton")); // Ensure the indicator moves to the light button
  } else if (theme === 'dark') {
    dark(true);
    updateIndicator(document.getElementById("darkButton")); // Ensure the indicator moves to the dark button
  } else {
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
      dark(true);
      updateIndicator(document.getElementById("darkButton")); // If system preference is dark
    } else {
      light(true);
      updateIndicator(document.getElementById("lightButton")); // If system preference is light
    }
  }
}

// Initialize the theme and indicator position on page load
systemDefault();

// Add event listeners to ensure the glow moves when buttons are clicked
document.getElementById("lightButton").addEventListener("click", () => light(false));
document.getElementById("darkButton").addEventListener("click", () => dark(false));
document.getElementById("defaultButton").addEventListener("click", () => {
  systemDefault();
  updateIndicator(document.getElementById("defaultButton")); // Move indicator to the default button
});

