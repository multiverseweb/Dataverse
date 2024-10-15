// Array of city names
var cities = ["Pune", "Moradabad", "Dehradun","Rampur","Delhi","Coimbatore"];

// /preloader js styling
let preloader = document.querySelector("#preloader");
window.addEventListener("load",function(e){
    preloader.style.display = "none";
    displayCopyright();
});

const goTopBtn = document.querySelector('.go-top-btn');

window.addEventListener('scroll', checkHeight)

function checkHeight(){
  if(window.scrollY > 200) {
    goTopBtn.style.display = "flex"
  } else {
    goTopBtn.style.display = "none"
  }
}

goTopBtn.addEventListener('click', () => {
  window.scrollTo({
    top: 0,
    behavior: "smooth"
  })
})

function changeCss() {
    var top = document.getElementById("top");
    var scroll_icon = document.getElementById("scroll_icon");
    (this.scrollY > 30 && this.scrollY < 2450) ? top.style.opacity = 1 : top.style.opacity = 0;
    (this.scrollY > 0) ? scroll_icon.style.opacity = 0 : scroll_icon.style.opacity = 1;
}

window.addEventListener("scroll", changeCss, false);


var map = L.map('map', {
    center: [23.7937, 80.9629],
    zoom: 5,
    zoomControl: false
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
async function addMarker(city) {
    var url = `https://nominatim.openstreetmap.org/search?format=json&q=${city}`;
    
    try {
        const response = await fetch(url, {
            headers: {
                'User-Agent': 'YourAppName/1.0' // Replace with your app name
            }
        });
        const data = await response.json();
        
        if (data.length > 0) {
            var lat = data[0].lat;
            var lon = data[0].lon;
            L.marker([lat, lon], { icon: redIcon }).addTo(map)
              .bindPopup(city);
        } else {
            console.log("No results found for " + city);
        }
    } catch (error) {
        console.error("Error fetching coordinates for " + city + ": " + error);
    }
}

// Add markers for each city
cities.forEach(city => addMarker(city));


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
var examples2 = document.getElementById("examples2");
var tags = document.getElementById("tags");
var contribute = document.getElementById("contribute");
var github = document.getElementById("github");
var last_link = document.getElementById("last_link");
var indicator = document.getElementById("indicator");
var shadow = document.getElementById("shadow");
var download = document.getElementById("download_btn");
const lightButton = document.getElementById("lightButton");
const darkButton = document.getElementById("darkButton");


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


// function updateIndicator(button) {
//   // Set the position of the indicator to align with the selected button
//   const adjustment = (button.offsetHeight - indicator.offsetHeight) / 2;
//   indicator.style.top = `${button.offsetTop + adjustment}px`;

//   // Set the glow effect based on the theme
//   const currentTheme = localStorage.getItem('theme');
//   if (currentTheme === 'light') {
//       indicator.style.backgroundImage = "radial-gradient(circle, rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0) 70%)"; // Black glow in light mode
//       // indicator.style.boxShadow = "0 0 5px 3px rgba(0, 0, 0, 0.7)"; // Adjust the box-shadow radius and spread here
//   } else {
//       indicator.style.backgroundImage = "radial-gradient(circle, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0) 70%)"; // White glow in dark mode
//       // indicator.style.boxShadow = "0 0 5px 3px rgba(255, 255, 255, 0.7)"; // Adjust the box-shadow radius and spread here
//   }
// }

function updateIndicator(button) {
  const adjustment = (button.offsetHeight - indicator.offsetHeight) / 2;
  indicator.style.top = `${button.offsetTop + adjustment}px`;

  const currentTheme = localStorage.getItem('theme');
  if (currentTheme === 'light') {
      indicator.style.backgroundImage = "radial-gradient(circle, rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0))"; // Black glow for light mode
      // indicator.style.boxShadow = "0 0 5px 3px rgba(0, 0, 0, 0.7)"; // Subtle black glow
  } else {
      indicator.style.backgroundImage = "radial-gradient(circle, rgba(255, 255, 255, 0.7), rgba(0, 0, 0, 0))"; // White glow for dark mode
      // indicator.style.boxShadow = "0 0 5px 3px rgba(255, 255, 255, 0.7)"; // Subtle white glow
  }
}



function light(flag) {
  localStorage.setItem('theme', 'light');
  body.classList.remove('dark-mode');
  body.classList.add('light-mode');

  const lightButton = document.getElementById("lightButton");
  updateIndicator(lightButton); // Update the indicator position and style for the light button
}

function dark(flag) {
  localStorage.setItem('theme', 'dark');
  body.classList.remove('light-mode');
  body.classList.add('dark-mode');

  const darkButton = document.getElementById("darkButton");
  updateIndicator(darkButton); // Update the indicator position and style for the dark button
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
      // Fallback based on system preference
      if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
          dark(true);
          updateIndicator(document.getElementById("darkButton")); // If system preference is dark
      } else {
          light(true);
          updateIndicator(document.getElementById("lightButton")); // If system preference is light
      }
  }

  // Move indicator to the default button when explicitly selected
  updateIndicator(defaultButton);
}

// Initialize the theme and indicator position on page load
systemDefault();
document.getElementById("lightButton").addEventListener("click", () => {
  light(false);
  updateIndicator(document.getElementById("lightButton"));
});
document.getElementById("darkButton").addEventListener("click", () => {
  dark(false);
  updateIndicator(document.getElementById("darkButton"));
});
document.getElementById("defaultButton").addEventListener("click", () => {
  systemDefault();
  updateIndicator(document.getElementById("defaultButton"));
});


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

let scrollSpeed = 2;
let currentSpeed = scrollSpeed;
let autoScroll = true;
let scrollTimeout;

// Function to scroll the 'examples' and 'examples2' div automatically
function autoScrollExamples() {
    if (autoScroll) {
        examples.scrollLeft += currentSpeed;
        examples2.scrollLeft += currentSpeed * 1.2;

        // Looping the scroll
        if (examples.scrollLeft + examples.clientWidth >= examples.scrollWidth) {
            examples.scrollLeft = 0;
        }
        if (examples2.scrollLeft + examples2.clientWidth >= examples2.scrollWidth) {
            examples2.scrollLeft = 0;
        }
    }
}

setInterval(autoScrollExamples, 30);

// Smoothly adjust scroll speed
const adjustSpeed = (targetSpeed) => {
    clearInterval(scrollTimeout);
    scrollTimeout = setInterval(() => {
        if (currentSpeed !== targetSpeed) {
            currentSpeed += (targetSpeed > currentSpeed ? 0.1 : -0.3);
            currentSpeed = Math.abs(currentSpeed - targetSpeed) < 0.1 ? targetSpeed : currentSpeed;
        } else {
            clearInterval(scrollTimeout);
        }
    }, 30);
};

// Hovering behavior with smooth stop/resume
const stopAutoScroll = () => {
    autoScroll = false;
    adjustSpeed(0);
};

const startAutoScroll = () => {
    autoScroll = true;
    adjustSpeed(scrollSpeed);
};

examples.addEventListener("mouseenter", stopAutoScroll);
examples.addEventListener("mouseleave", startAutoScroll);
examples2.addEventListener("mouseenter", stopAutoScroll);
examples2.addEventListener("mouseleave", startAutoScroll);

window.addEventListener("scroll", progress);


function showCustomAlert(message) {
  document.getElementById('alert-message').innerText = message;
  document.getElementById('custom-alert').style.display = 'block';
}

function closeCustomAlert() {
  document.getElementById('custom-alert').style.display = 'none';
}

/*CHANGING DIRECTION OF AEROPLANE*/

function updateAngle() {
  let randomAngle = Math.floor(Math.random() * 360) + 'deg';
  document.documentElement.style.setProperty('--angle', randomAngle);
}

setInterval(updateAngle, 10000);

function validateForm() { 
  const name = document.querySelector('input[name="Name"]').value.trim();
  const email = document.querySelector('input[name="Email"]').value.trim();
  const message = document.querySelector('textarea[name="Message"]').value.trim();

  console.log("Name:", name);
  console.log("Email:", email);
  console.log("Message:", message);

  if (!name) {
      alert("Please enter your name.");
      return false;
  }
  if (!email) {
      alert("Please enter your email.");
      return false;
  }
  if (!message) {
      alert("Please enter your message.");
      return false;
  }
  
  return true;
}

// FORM VALIDATING FUNCTION
function validateForm() {

  const nameInput = document.querySelector('[name="Name"]');
  const emailInput = document.querySelector('[name="Email"]');
  const messageInput = document.querySelector('[name="Message"]');


  if (nameInput.value === '') {
      alert('Please enter your name.');
      return false;
  }
  
  if (!isValidEmail(emailInput.value)) {
    alert('Please enter a valid email address.');
    return false;
  }
  
  if (messageInput.value === '') {
      alert('Please enter your message.');
      return false;
  }
  
  
  const formData = {
    Name: nameInput.value,
    Email: emailInput.value,
    Message: messageInput.value
  };
  localStorage.setItem('reviewData', JSON.stringify(formData));
  
  nameInput.value = '';
  emailInput.value = '';
  messageInput.value = '';
    
  alert('Your feedback has been submitted');

  return false;
} 
  
// EMAIL VALIDATING FUNCTION 
function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

// Display the current year in the copyright section
function displayCopyright() {
  const year = new Date().getFullYear();
  document.getElementById("copyright").innerText = year;
}