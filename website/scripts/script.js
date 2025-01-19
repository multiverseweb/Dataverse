import { showModal, closeModal, attachToWindow } from "./sharedUtilities.js";
// Array that holds all functions need to be accessible for HTML
var windowFunctions = [];

// Array of city names
var cities = [
  "Pune",
  "Moradabad",
  "Dehradun",
  "Rampur",
  "Delhi",
  "Coimbatore",
  "Riyadh",
  "Ahmedabad",
  "Kolkata",
  "Mumbai",
  "Jorhat",
  "Arrah",
  "Bhopal",
  "Bengalore",
  "Secunderabad",
  "Ludhiana",
  "Nagpur",
  "Lucknow",
  "Gorakhpur",
  "Bhilai",
  "Kanpur",
  "Panaji",
  "Dhamtari",
  "Vijaywada",
  "Ujjain",
  "Sydney",
];

try {
  var map = L.map("map", {
    center: [22.7937, 77.9629],
    zoom: 4,
    zoomControl: false,
  });

  // Add OpenStreetMap tile layer
  L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
    attribution:
      '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
  }).addTo(map);

  var redIcon = L.icon({
    iconUrl:
      "https://img1.picmix.com/output/stamp/normal/2/5/4/3/873452_376bb.png",
    iconSize: [20, 20],
    iconAnchor: [12, 12],
    popupAnchor: [1, -34],
    shadowSize: [41, 41],
  });
} catch (e) {
  console.error(e);
}

// Your OpenCage API Key here
const OPENCAGE_API_KEY = "3f55c6e93c2c4b19ae45f1fd5db12cfc";

// Function to get coordinates for a city and add a marker using OpenCage API
async function addMarker(city) {
  var url = `https://api.opencagedata.com/geocode/v1/json?q=${city}&key=${OPENCAGE_API_KEY}`;

  try {
    const response = await fetch(url);

    if (!response.ok)
      throw new Error(`Network response was not ok: ${response.statusText}`);

    const data = await response.json();

    if (data.results.length > 0) {
      const lat = data.results[0].geometry.lat;
      const lon = data.results[0].geometry.lng;
      L.marker([lat, lon], { icon: redIcon }).addTo(map).bindPopup(city);
    } else {
      console.log("No results found for " + city);
    }
  } catch (error) {
    console.error("Error fetching coordinates for " + city + ": " + error);
  }
}

// Function to add markers with a delay to respect API limits
async function addMarkersWithDelay(cities) {
  for (let i = 0; i < cities.length; i++) {
    await addMarker(cities[i]);
    await new Promise((resolve) => setTimeout(resolve, 1000)); // 1-second delay between requests
  }
}

// Call the function to add markers
addMarkersWithDelay(cities);

// /preloader js styling and other stuff needed for preload
window.addEventListener("DOMContentLoaded", () => {
  // Hide the loader after 3 seconds
  setTimeout(() => {
    const loader = document.getElementById("video-loader");
    if (loader) {
      loader.style.display = "none";
    }

    displayCopyright();
  }, 3000);

  attachToWindow(windowFunctions);
});
function topFunction() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}
windowFunctions.push(topFunction);
function changeCss() {
  var top = document.getElementById("top");
  var scroll_icon = document.getElementById("scroll_icon");
  if (scroll_icon) {
    this.scrollY > 30 ? (top.style.opacity = 1) : (top.style.opacity = 0);
    this.scrollY > 0
      ? (scroll_icon.style.opacity = 0)
      : (scroll_icon.style.opacity = 1);
  }
}

window.addEventListener("scroll", changeCss, false);

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
const technologies = document.getElementById("technologies");
var footer = document.getElementById("footer");
var links = document.getElementById("linksTejas");
var endLogo = document.getElementById("end-logo");
var feedbackForm = document.getElementById("feedback-form");

let lastScrollTop = 0;
const navbar = document.getElementById("navbar");

window.addEventListener("scroll", () => {
  const scrollTop = window.pageYOffset || document.documentElement.scrollTop;

  if (scrollTop > lastScrollTop) {
    // Scroll down
    navbar.style.top = "-60px";
    burger.style.top = "-60px";
    lines.style.top = "-60px";
    cross.style.top = "-60px";
  } else {
    // Scroll up
    navbar.style.top = "0";
    burger.style.top = "10px";
    lines.style.top = "10px";
    cross.style.top = "10px";
  }

  lastScrollTop = scrollTop;
});

let lastScroll = 0;
function progress() {
  var scroll = this.scrollY;
  var scrollHeight =
    document.documentElement.scrollHeight -
    document.documentElement.clientHeight;
  var percent = Math.round((scroll / scrollHeight) * 100);
  document.getElementById("progress_bar").style.width = percent + "vw";
}

window.addEventListener("scroll", progress);

function show() {
  l2.style.opacity = 0;
  l1.style.transform = "rotate(-45deg)";
  l3.style.transform = "rotate(45deg)";
  burger.style.display = "none";
  cross.style.display = "block";
  plane.style.right = 0;
  document.body.style.overflowY = "hidden";
  buttons.style.marginLeft = 0;
}
windowFunctions.push(show);

function hide() {
  l2.style.opacity = 1;
  l1.style.transform = "rotate(0deg)";
  l3.style.transform = "rotate(0deg)";
  burger.style.display = "block";
  cross.style.display = "none";
  plane.style.right = "-100vw";
  document.body.style.overflowY = "scroll";
  buttons.style.marginLeft = "-60px";
}
windowFunctions.push(hide);

function updateIndicator(button) {
  const adjustment = (button.offsetHeight - indicator.offsetHeight) / 2;
  indicator.style.top = `${button.offsetTop + adjustment}px`;

  const currentTheme = localStorage.getItem("theme");
  if (currentTheme === "light") {
    indicator.style.backgroundImage =
      "radial-gradient(circle, rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0))"; // Black glow for light mode
    // indicator.style.boxShadow = "0 0 5px 3px rgba(0, 0, 0, 0.7)"; // Subtle black glow
  } else {
    indicator.style.backgroundImage =
      "radial-gradient(circle, rgba(255, 255, 255, 0.7), rgba(0, 0, 0, 0))"; // White glow for dark mode
    // indicator.style.boxShadow = "0 0 5px 3px rgba(255, 255, 255, 0.7)"; // Subtle white glow
  }
}
windowFunctions.push(updateIndicator);

function light(flag) {
  localStorage.setItem("theme", "light");
  document.body.classList.remove("dark-mode");
  document.body.classList.add("light-mode");
  if (
    document.getElementById("map") &&
    tags &&
    contribute &&
    shadow &&
    technologies
  ) {
    document.getElementById("map").style.filter = "none";
    document.getElementById("map").style.zIndex = 0;
    tags.style.borderColor = "black";
    tags.style.backgroundColor = "#00000000";
    contribute.style.filter = "invert(1)";
    shadow.style.backgroundImage =
      "linear-gradient(115deg, #00000000,#f9f9f9,#00000000)";
    technologies.style.border = "1px solid #000000";
    /*footer.style.backgroundColor="#ffffff";
    footer.style.color="#000000";
    links.style.backgroundColor="#ffffff";
    links.style.color="#000000";*/
    footer.style.filter = "invert(1)";
    links.style.filter = "invert(1)";
    endLogo.style.filter = "invert(1)";
  }
  indicator.style.backgroundImage =
    "radial-gradient(rgba(0,0,0, 0.608),#00000000,#00000000)";
  const lightButton = document.getElementById("lightButton");
  updateIndicator(lightButton); // Update the indicator position and style for the light button
}
windowFunctions.push(light);

function dark(flag) {
  if (
    document.getElementById("map") &&
    tags &&
    contribute &&
    shadow &&
    technologies
  ) {
    document.getElementById("map").style.filter =
      "invert(1) hue-rotate(180deg) brightness(1.7)";
    tags.style.borderColor = "rgba(255, 255, 255, 0.323)";
    tags.style.backgroundColor = "#00000000";
    shadow.style.backgroundImage =
      "linear-gradient(115deg, #00000000,#000000d4,#00000000)";
    contribute.style.filter = "invert(0)";
    technologies.style.border = "1px solid #ffffff44";
    /*footer.style.backgroundColor="#000000";
    footer.style.color="#ffffff";
    links.style.backgroundColor="#000000";
    links.style.color="#ffffff";*/
    footer.style.filter = "invert(0)";
    links.style.filter = "invert(0)";
    endLogo.style.filter = "invert(0)";
  }
  localStorage.setItem("theme", "dark");
  indicator.style.backgroundImage =
    "radial-gradient(rgba(255,255,255, 0.608),#00000000,#00000000)";
  document.body.classList.remove("light-mode");
  document.body.classList.add("dark-mode");

  const darkButton = document.getElementById("darkButton");
  updateIndicator(darkButton); // Update the indicator position and style for the dark button
}
windowFunctions.push(dark);

function systemDefault() {
  const theme = localStorage.getItem("theme");
  const defaultButton = document.getElementById("defaultButton");

  if (theme === "light") {
    light(true);
    updateIndicator(document.getElementById("lightButton")); // Ensure the indicator moves to the light button
  } else if (theme === "dark") {
    dark(true);
    updateIndicator(document.getElementById("darkButton")); // Ensure the indicator moves to the dark button
  } else {
    // Fallback based on system preference
    if (
      window.matchMedia &&
      window.matchMedia("(prefers-color-scheme: dark)").matches
    ) {
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
windowFunctions.push(systemDefault);
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

let scrollSpeed = 2;
let currentSpeed = scrollSpeed;
let autoScroll = true;
let scrollTimeout;

// Function to scroll the 'examples' and 'examples2' div automatically
function autoScrollExamples() {
  if ((examples, examples2)) {
    if (autoScroll) {
      examples.scrollLeft += currentSpeed;
      examples2.scrollLeft += currentSpeed * 1.2;

      // Looping the scroll
      if (examples.scrollLeft + examples.clientWidth >= examples.scrollWidth) {
        examples.scrollLeft = 0;
      }
      if (
        examples2.scrollLeft + examples2.clientWidth >=
        examples2.scrollWidth
      ) {
        examples2.scrollLeft = 0;
      }
    }
  }
}

setInterval(autoScrollExamples, 30);

// Smoothly adjust scroll speed
const adjustSpeed = (targetSpeed) => {
  clearInterval(scrollTimeout);
  scrollTimeout = setInterval(() => {
    if (currentSpeed !== targetSpeed) {
      currentSpeed += targetSpeed > currentSpeed ? 0.1 : -0.3;
      currentSpeed =
        Math.abs(currentSpeed - targetSpeed) < 0.1 ? targetSpeed : currentSpeed;
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

if ((examples, examples2)) {
  examples.addEventListener("mouseenter", stopAutoScroll);
  examples.addEventListener("mouseleave", startAutoScroll);
  examples2.addEventListener("mouseenter", stopAutoScroll);
  examples2.addEventListener("mouseleave", startAutoScroll);
}

window.addEventListener("scroll", progress);

/*CHANGING DIRECTION OF AEROPLANE*/

function updateAngle() {
  let randomAngle = Math.floor(Math.random() * 360) + "deg";
  document.documentElement.style.setProperty("--angle", randomAngle);
}

setInterval(updateAngle, 10000);

/*VALIDATE FORM AND CALL BACKEND*/
window.onload = function () {
  let feedbackField;
  if (document.forms["feedback-form"]) {
    feedbackField = document.forms["feedback-form"]["Message"];

    feedbackField.addEventListener("focus", () => {
      checkFeedbackLength(feedbackField);
    });

    feedbackField.addEventListener("blur", () => {
      document.getElementById("feedbackError").style.opacity = "0%";
    });
  }
};

function validateForm(event) {
  event.preventDefault(); // Prevent form from submitting by default

  const nameInput = document.querySelector('[name="Name"]');
  const emailInput = document.querySelector('[name="Email"]');
  const messageInput = document.querySelector('textarea[name="Message"]');
  const rating = document.querySelector('[name="rating"]:checked'); // Get the checked rating

  if (nameInput.value === "") {
    alert("Please enter your name.");
    return false;
  }

  if (!isValidEmail(emailInput.value)) {
    alert("Please enter a valid email address.");
    return false;
  }

  if (messageInput.value === "") {
    alert("Please enter your message.");
    return false;
  }

  if (!rating) {
    alert("Please select a rating.");
    return false;
  }

  if (!checkFeedbackLength(messageInput)) {
    return false;
  }

  const formData = new FormData();
  formData.append("Name", nameInput.value);
  formData.append("Email", emailInput.value);
  formData.append("Message", messageInput.value);
  formData.append("Rating", rating.value);

  // Send the form data to FastAPI using fetch
  fetch("http://127.0.0.1:8000/submit_feedback", {
    method: "POST",
    body: formData, // Send as form data
  })
    .then((response) => response.json()) // Parse JSON response from FastAPI
    .then((data) => {
      // Handle the response from the FastAPI backend (success or error)
      if (data.success) {
        showModal("Thank you for your feedback!", "submit feedback");
        // Clear form fields after submission
        nameInput.value = "";
        emailInput.value = "";
        messageInput.value = "";
        const selectedRating = document.querySelector(
          '[name="rating"]:checked'
        );
        if (selectedRating) {
          selectedRating.checked = false; // Uncheck the selected radio button
        }
      } else {
        alert("Something went wrong, please try again.");
      }
    })
    .catch((error) => {
      console.error("Error:", error);
      alert("An error occurred. Please try again.");
    });

  return false;
}

function checkFeedbackLength(input) {
  if (input.value.length < 10) {
    document.getElementById("feedbackError").style.opacity = "100%";
    return false;
  } else {
    document.getElementById("feedbackError").style.opacity = "0%";
    return true;
  }
}
window.checkFeedbackLength = checkFeedbackLength;
window.validateForm = validateForm;

// EMAIL VALIDATING FUNCTION
function isValidEmail(email) {
  const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
  return emailRegex.test(email);
}

// Display the current year in the copyright section
function displayCopyright() {
  const year = new Date().getFullYear();
  if ((document.getElementById("copyright").innerText = year)) {
    document.getElementById("copyright").innerText = year;
  }
}

ScrollReveal().reveal(".reveal", {
  distance: "150px",
  duration: 600,
  easing: "ease-in-out",
  origin: "bottom",
  interval: 100, // Delay between revealing multiple elements
});
windowFunctions.push(ScrollReveal);

export { windowFunctions };
