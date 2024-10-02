// Array of city names
var cities = ["Pune", "Moradabad", "Dehradun", "Delhi"];

// Log message
console.log("Tejas' Codes :)");

// DOM Elements
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
var examples2 = document.getElementById("examples2");
var tags = document.getElementById("tags");
var contribute = document.getElementById("contribute");
var github = document.getElementById("github");
var last_link = document.getElementById("last_link");
var indicator = document.getElementById("indicator");
var shadow = document.getElementById("shadow");
var download = document.getElementById("download_btn");

let lastScrollTop = 0;
const navbar = document.querySelector('.navbar');

// Scroll event listener
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

// Functions to show/hide menu
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

// Theme management functions
function systemDefault() {
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

systemDefault();
indicator.style.top = "95px";

// Light and dark mode functions
function light(flag) {
  localStorage.setItem('theme', 'light');
  document.getElementById("map").style.filter = "none";
  document.getElementById("map").style.zIndex = 0;
  body.style.backgroundColor = "#e8e8e8";
  body.style.color = "black";
  tags.style.borderColor = "black";
  tags.style.backgroundColor = "#171717";
  contribute.style.borderColor = "black";
  contribute.style.color = "black";
  download.style.borderColor = "black";
  download.style.color = "black";

  contribute.addEventListener("mouseenter", contributeHoverEffect);
  contribute.addEventListener("mouseleave", contributeHoverEffect);
  
  github.style.filter = "invert(0)";
  last_link.style.color = "black";
  
  if (flag == true) {
    indicator.style.top = "95px";
  } else {
    indicator.style.top = "52px";
  }
  
  indicator.style.backgroundImage = "radial-gradient(rgba(0,0,0, 0.608),#00000000,#00000000)";
  shadow.style.backgroundImage = "linear-gradient(115deg, #00000000,#e8e8e8,#00000000)";
  
  download.addEventListener("mouseenter", (event) => {
    event.target.style.color = "white";
    event.target.style.backgroundColor = "black";
  });
  download.addEventListener("mouseleave", (event) => {
    event.target.style.color = "black";
    event.target.style.backgroundColor = "#e8e8e8";
  });
}

function dark(flag) {
  localStorage.setItem('theme', 'dark');
  document.getElementById("map").style.filter = "invert(1) hue-rotate(180deg) brightness(1.5)";
  body.style.backgroundColor = "black";
  body.style.color = "white";
  tags.style.borderColor = "rgba(255, 255, 255, 0.323)";
  tags.style.backgroundColor = "#00000000";
  download.style.borderColor = "white";
  download.style.color = "white";
  contribute.style.borderColor = "white";
  
  contribute.addEventListener("mouseenter", contributeHoverEffect);
  contribute.addEventListener("mouseleave", contributeHoverEffect);
  
  last_link.style.color = "white";
  
  if (flag == true) {
    indicator.style.top = "95px";
  } else {
    indicator.style.top = "52px";
  }
  
  indicator.style.backgroundImage = "radial-gradient(rgba(255,255,255, 0.608),#00000000,#00000000)";
  shadow.style.backgroundImage = "linear-gradient(115deg, #00000000,#000000d4,#00000000)";
  
  download.addEventListener("mouseenter", (event) => {
    event.target.style.color = "black";
    event.target.style.backgroundColor = "white";
  });
  download.addEventListener("mouseleave", (event) => {
    event.target.style.color = "white";
    event.target.style.backgroundColor = "black";
  });
}

// Scroll functions
function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}

function changeCss() {
  var top = document.getElementById("top");
  var scroll_icon = document.getElementById("scroll_icon");
  (window.scrollY > 30 && window.scrollY < 2450) ? top.style.opacity = 1 : top.style.opacity = 0;
  (window.scrollY > 0) ? scroll_icon.style.opacity = 0 : scroll_icon.style.opacity = 1;
}

// Event listener for scroll
window.addEventListener("scroll", () => {
  changeCss();
  animate();
  progress();
}, false);

// Animation function
function animate() {
  var reveal = document.querySelectorAll(".section");

  for (var i = 1; i < reveal.length; i++) {
    var windowHeight = window.innerHeight;
    var elementTop = reveal[i].getBoundingClientRect().top;
    var e = 90;

    if (elementTop < windowHeight - e) {
      reveal[i].classList.add("big_container");
    } else {
      reveal[i].classList.remove("big_container");
    }
  }
}

// Progress function
let lastScroll = 0;
function progress() {
  var scroll = window.scrollY;
  var percent = Math.round((scroll / 3000) * 100);
  document.getElementById("progress_bar").style.width = percent + 'vw';
  if (scroll > lastScroll) {
    examples.scrollLeft += percent / 15;
    examples2.scrollLeft += percent / 10;
  } else {
    examples.scrollLeft -= percent / 15;
    examples2.scrollLeft -= percent / 10;
  }
  lastScroll = scroll;
}

// Map initialization
var map = L.map('map', {
  center: [23.7937, 74.9629],
  zoom: 4,
  zoomControl: false
});

// Add OpenStreetMap tile layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Red icon for markers
var redIcon = L.icon({
  iconUrl: 'https://img1.picmix.com/output/stamp/normal/2/5/4/3/873452_376bb.png',
  iconSize: [25, 25],
  iconAnchor: [12, 12],
  popupAnchor: [1, -34],
  shadowSize: [41, 41]
});

// Function to validate and sanitize input
function sanitizeInput(city) {
  // Remove any non-alphanumeric characters (except spaces)
  return city.replace(/[^a-zA-Z\s]/g, '').trim();
}

// Function to get coordinates for a city and add a marker
function addMarker(city) {
  var sanitizedCity = sanitizeInput(city);
  
  if (!sanitizedCity) {
    console.warn(`Invalid city name: ${city}`);
    showCustomAlert(`Invalid city name: ${city}`);
    return;
  }

  var url = `https://nominatim.openstreetmap.org/search?format=json&q=${encodeURIComponent(sanitizedCity)}`;
  
  fetch(url)
    .then(response => response.json())
    .then(data => {
      if (data.length > 0) {
        var lat = data[0].lat;
        var lon = data[0].lon;
        L.marker([lat, lon], { icon: redIcon }).addTo(map)
          .bindPopup(sanitizedCity);
      } else {
        console.warn(`No coordinates found for city: ${sanitizedCity}`);
        showCustomAlert(`Could not find coordinates for ${sanitizedCity}`);
      }
    })
    .catch(error => {
      console.error(`Error fetching coordinates for ${sanitizedCity}: `, error);
      showCustomAlert(`Failed to get coordinates for ${sanitizedCity}`);
    });
}

// Add markers for each city
cities.forEach(city => addMarker(city));

// Custom alert functions
function showCustomAlert(message) {
  document.getElementById('alert-message').innerText = message;
  document.getElementById('custom-alert').style.display = 'block';
}

function closeCustomAlert() {
  document.getElementById('custom-alert').style.display = 'none';
}

// Aeroplane direction update function
function updateAngle() {
  let randomAngle = Math.random() * 10 + 70;
  plane.style.transform = `rotate(${randomAngle}deg)`;
}
setInterval(updateAngle, 1000);

// Hover effect for contribute button
function contributeHoverEffect(event) {
  if (event.type === 'mouseenter') {
    event.target.style.color = "white";
    event.target.style.backgroundColor = "black";
    github.style.filter = "invert(1)";
  } else if (event.type === 'mouseleave') {
    event.target.style.color = "black";
    event.target.style.backgroundColor = "#e8e8e8";
    github.style.filter = "invert(0)";
  }
}

// Event listeners for click
burger.addEventListener("click", show);
cross.addEventListener("click", hide);

