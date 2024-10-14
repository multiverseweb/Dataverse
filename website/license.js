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
var licenseContents = document.querySelectorAll('.license-content');
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

function systemDefault() {
  displayCopyright();
  const theme = localStorage.getItem('theme');

  if (theme === 'light') {
    light(true);
    shadow.style.backgroundImage = "linear-gradient(115deg, #00000000,#e8e8e8,#00000000)";
  } else if (theme === 'dark') {
    dark(true);
  } else {
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
      dark(true);
    } else {
      light(true);
    }
  }
}

function light(flag) {
  localStorage.setItem('theme', 'light');
  body.style.backgroundColor = "white";
  body.style.color = "black";

  licenseContents.forEach(content => {
    content.style.backgroundColor = "#e8e8e8"; 
    content.style.color = "black"; 
  });

  if (flag == true) {
    indicator.style.top = "95px";
  }
  else {
    indicator.style.top = "52px";
  }
  indicator.style.backgroundImage = "radial-gradient(rgba(0,0,0, 0.608),#00000000,#00000000)";
  shadow.style.backgroundImage = "linear-gradient(115deg, #00000000,#e8e8e8,#00000000)";
}

function dark(flag) {
  localStorage.setItem('theme', 'dark');
  body.style.backgroundColor = "black";
  body.style.color = "white";

  licenseContents.forEach(content => {
    content.style.backgroundColor = "black"; 
    content.style.color = "white"; 
  });

  if (flag == true) {
    indicator.style.top = "95px";
  }
  else {
    indicator.style.top = "52px";
  }
  indicator.style.backgroundImage = "radial-gradient(rgba(255,255,255, 0.608),#00000000,#00000000)";
  shadow.style.backgroundImage = "linear-gradient(115deg, #00000000,#000000d4,#00000000)";
}

// Display the current year in the copyright section
function displayCopyright() {
  const year = new Date().getFullYear();
  document.getElementById("copyright").innerText = year;
}

systemDefault();