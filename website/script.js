// Array of city names
var cities = ["Pune", "Moradabad"];

console.log("Tejas' Codes :)");

var l1 = document.getElementById("l1");
var l2 = document.getElementById("l2");
var l3 = document.getElementById("l3");
var burger = document.getElementById("burger");
var lines = document.getElementById("lines");
var cross = document.getElementById("cross");
var plane = document.getElementById("plane");
var body = document.getElementById("body");
var buttons = document.getElementById("buttons");
var examples = document.getElementById("examples");
var tags = document.getElementById("tags");
var contribute = document.getElementById("contribute");
var github = document.getElementById("github");
var last_link = document.getElementById("last_link");
var indicator = document.getElementById("indicator");
var shadow = document.getElementById("shadow");
var download = document.getElementById("download_btn");

let lastScrollTop = 0;
const navbar = document.querySelector('navbar');

window.addEventListener('scroll', () => {
  const scrollTop = window.pageYOffset || document.documentElement.scrollTop;

  if (scrollTop > lastScrollTop) {
    // Scroll down
    navbar.style.top = '-60px';
    burger.style.top = '-60px';
    lines.style.top = '-60px';
    cross.style.top = '-60px';
  } else {
    // Scroll up
    navbar.style.top = '0';
    burger.style.top = '10px';
    lines.style.top = '10px';
    cross.style.top = '10px';
  }

  lastScrollTop = scrollTop;
});

function copy() {
  navigator.clipboard.writeText("multiverse-dataverse.netlify.app");
  document.getElementById("copy").innerHTML = "✓";
}

function download_prompt() {
  alert("Dataverse is currently under development. It will be available for installastion soon.");
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

function light(flag) {
  document.getElementById("map").style.filter = "none";
  document.getElementById("map").style.zIndex = 0;
  body.style.backgroundColor = "#e8e8e8";
  body.style.color = "black";
  examples.style.backgroundColor = "#e8e8e8";
  tags.style.borderColor = "black";
  tags.style.backgroundColor = "#171717";
  contribute.style.borderColor = "black";
  contribute.style.color = "black";
  download.style.borderColor = "black";
  download.style.color = "black";
  contribute.addEventListener("mouseenter", (event) => {
    event.target.style.color = "white";
    github.style.filter = "invert(1)";
  });
  contribute.addEventListener("mouseleave", (event) => {
    event.target.style.color = "black";
    github.style.filter = "invert(0)";
  });
  contribute.addEventListener("mouseenter", (event) => { event.target.style.backgroundColor = "black" });
  contribute.addEventListener("mouseleave", (event) => { event.target.style.backgroundColor = "#e8e8e8" });
  github.style.filter = "invert(0)";
  last_link.style.color = "black";
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
  document.getElementById("map").style.filter = "invert(1) hue-rotate(180deg) brightness(1.5)";
  body.style.backgroundColor = "black";
  body.style.color = "white";
  examples.style.backgroundColor = "#161616";
  tags.style.borderColor = "rgba(255, 255, 255, 0.323)";
  tags.style.backgroundColor = "#00000000";
  download.style.borderColor = "white";
  download.style.color = "white";
  contribute.style.borderColor = "white";
  contribute.addEventListener("mouseenter", (event) => { event.target.style.color = "black" });
  contribute.addEventListener("mouseleave", (event) => { event.target.style.color = "white" });
  contribute.addEventListener("mouseenter", (event) => {
    event.target.style.backgroundColor = "white";
    github.style.filter = "invert(0)";
  });
  contribute.addEventListener("mouseleave", (event) => {
    event.target.style.backgroundColor = "black";
    github.style.filter = "invert(1)"
  });
  last_link.style.color = "white";
  if (flag == true) {
    indicator.style.top = "95px";
  }
  else {
    indicator.style.top = "10px";
  }
  indicator.style.backgroundImage = "radial-gradient(rgba(255,255,255, 0.608),#00000000,#00000000)";
  shadow.style.backgroundImage = "linear-gradient(115deg, #00000000,#000000d4,#00000000)";
}

function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}
function changeCss() {
  var top = document.getElementById("top");
  var scroll_icon = document.getElementById("scroll_icon");
  (this.scrollY > 30 && this.scrollY < 2450) ? top.style.opacity = 1 : top.style.opacity = 0;
  (this.scrollY > 0) ? scroll_icon.style.opacity = 0 : scroll_icon.style.opacity = 1;
}

window.addEventListener("scroll", changeCss, false);


function animate() {
  var reveal = document.querySelectorAll(".section");

  for (var i = 1; i < reveal.length; i++) {
    var windowHeight = window.innerHeight;
    var elementTop = reveal[i].getBoundingClientRect().top;
    var e = 90;

    if (elementTop < windowHeight - e) {
      reveal[i].classList.add("big_container");
    }
    else {
      reveal[i].classList.remove("big_container");
    }
  }
}

window.addEventListener("scroll", animate);


function progress() {
  var scroll = this.scrollY;
  var percent = Math.round((scroll / 2870) * 100);
  document.getElementById("progress_bar").style.width = percent + 'vw';
};

window.addEventListener("scroll", progress);


var map = L.map('map', {
  center: [22.5937, 79.9629],
  zoom: 3,
  zoomControl: false // Disable the default zoom control
});
// Add OpenStreetMap tile layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

var redIcon = L.icon({
  iconUrl: 'https://img1.picmix.com/output/stamp/normal/2/5/4/3/873452_376bb.png',
  iconSize: [25, 25],
  iconAnchor: [12, 12],
  popupAnchor: [1, -34],
  shadowSize: [41, 41]
});

// Function to get coordinates for a city and add a marker
function addMarker(city) {
  var url = `https://nominatim.openstreetmap.org/search?format=json&q=${city}`;
  fetch(url)
    .then(response => response.json())
    .then(data => {
      if (data.length > 0) {
        var lat = data[0].lat;
        var lon = data[0].lon;
        L.marker([lat, lon], { icon: redIcon }).addTo(map)
          .bindPopup(city);
      } else {
        console.log("No results found for " + city);
      }
    })
    .catch(error => console.error("Error fetching coordinates for " + city + ": " + error));
}

// Add markers for each city
cities.forEach(city => addMarker(city));

function systemDefault() {
  if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
    dark(true);
    indicator.style.backgroundImage = "radial-gradient(rgba(255,255,255, 0.608),#00000000,#00000000)";
  } else {
    indicator.style.backgroundImage = "radial-gradient(rgba(0,0,0, 0.608),#00000000,#00000000)";
    light(true);
  }
}

systemDefault();
indicator.style.top = "95px";